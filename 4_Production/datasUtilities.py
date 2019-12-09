"""
Script qui va chercher les données des dernières 24h dans la base MySQL
"""
import pymysql.cursors
import pandas as pd
import urllib.request
import json
import datetime


def collectDatasFromTheDatabase():
    """
    Se connecte à la base de donnée et va y chercher les données des dernières 24h
    
    @return: True si tout a bien fonctionné, False sinon
    """    
    try:
        with open('db_informations.json') as json_file:
            infos = json.load(json_file)
                
        connection=pymysql.connect(host=infos["host"],
                               user=infos["user"],
                               passwd=infos["passwd"],
                               db=infos["db"],
                               cursorclass=pymysql.cursors.DictCursor)
        
        with connection.cursor() as cursor:
            sql = "SELECT time,TempExt,HygroExt FROM RecuperationDonnees WHERE time > DATE_SUB(NOW(), INTERVAL 24 HOUR) AND time <= NOW()"
            cursor.execute(sql)
            result = cursor.fetchall()
            
        #select the informations we want
        df = pd.DataFrame(result)
        df = df[["TempExt","HygroExt","time"]]
        df.index = df["time"]
        
    except:
        print("ECHEC DANS LA COLLECTE DES DONNEES DE LA RUCHE !")
        return(False)
    finally:
        connection.close()
    try:
        #resample the data    
        df = df.fillna(method='ffill')
        df = df.resample(rule='3H', base=0).mean()
        
        size = df.shape[0]
        
        while size > 8:
            df.drop(df.index[[0]], inplace=True)
            size = df.shape[0]
    
        df.to_csv("datas/Ruche24h.csv", index=True,sep=';')
    except:
        print("ECHEC DANS L'ENREGISTREMENT DES DONNEES DE LA RUCHE !")
        return(False)
    return(True)
    
    
def collectTheAirIQ():
    """
    get the air index quality of the last 2 days
    
    @return: True si tout a bien fonctionné, False sinon
    """
    #make a request:
    try:
        request = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=indice-qualite-de-lair&sort=date_ech&rows=2"
        with urllib.request.urlopen(request) as jsonfile:
            data = json.loads(jsonfile.read().decode())
    except:
        print("ECHEC LORS DE LA CONNEXION A L'API DE LA MEL !")
        return(False)
        
    #treat the response:
    try:
        listeDesRecords = data['records']
        listeDesFields = []
        for r in listeDesRecords: #on récupère chaque fields de données
            listeDesFields.append(r['fields']) 
        dico = []
        for k in listeDesFields:
            dico.append({'date' : k['date_ech'][0:10],'value' : k['valeur']})
        df = pd.DataFrame(dico)
        df.to_csv("datas/IQ24h.csv", index=False,sep=';')
    except:
        print("ECHEC LORS DU TRAITEMENT DES DONNEES DE L'API DE LA MEL !")
        return(False)
    return(True)
    
    
def mixIQandRuche():
    """
    Add the IQ field for each correponding day in the csv file with the datas 
    from the last 24 hours
    
    @return: True si tout a bien fonctionné, False sinon
    """
    try:
        dfMel = pd.read_csv("datas/IQ24h.csv", header=0, delimiter=';')
        dfRuche = pd.read_csv("datas/Ruche24h.csv", header=0, delimiter=';')
    except:
        print("ECHEC LORS DE L'OUVERTURE DES FICHIERS CSV !")
        return(False)
    try:
        listeDataJours = []
        for r in range(0,len(dfRuche)):
            a = dfRuche.at[r,"time"]
            a = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
            a = a.date()
        
            for m in range(0,len(dfMel)):    
                b = dfMel.at[m,"date"]
                b = datetime.datetime.strptime(b, '%Y-%m-%d')
                b = b.date()
                if b == a:
                        try :
                            listeDataJours.append({"Date" : dfRuche.at[r,"time"],
                                                   "temperature" : dfRuche.at[r,"TempExt"],
                                                   "humidite" : dfRuche.at[r,"HygroExt"],
                                                   "IQ" : dfMel.at[m,"value"]})
                        except:
                            print("Minor error")
    except:
        print("ECHEC LORS DU MELANGE DES 2 CSV !")
        return(False)
    
    try:
        df = pd.DataFrame(listeDataJours) 
        df.to_csv("datas/predictionData.csv", index=False,sep=';')
    except:
        print("ECHEC LORS DE L'ENREGISTREMENT DU CSV !")
        return(False)
    return(True) 
    
    
def savePrediction(prediction):
    """
    get the air index quality of the last 2 days
    
    @return: True si tout a bien fonctionné, False sinon
    """
    try:
        #load information from the database
        with open('db_informations.json') as json_file:
            infos = json.load(json_file)
                
        connection=pymysql.connect(host=infos["host"],
                               user=infos["user"],
                               passwd=infos["passwd"],
                               db=infos["db"],
                               cursorclass=pymysql.cursors.DictCursor)
        
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO airiq (time, prediction) VALUES ('" + str(datetime.datetime.now()) + "','" + str(prediction)+"')"
            
            cursor.execute(sql)
        connection.commit()
    except:
        print("ECHEC LORS DE L'ENREGISTREMENT DE LA PREDICTION DANS LA BASE SQL !")
        return(False)
    finally:
        connection.close()
    
    return(True)