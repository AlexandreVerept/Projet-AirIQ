"""
Ce programme sert à aller récupérer les données de qualité de l'air 
sur l'API de la MEL et créer un CSV avec ce qui est récupéré
"""

import urllib.request
import json
import pandas as pd

DEFAULTREQUEST = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=indice-qualite-de-lair&rows=5000"

def getRequest(request=DEFAULTREQUEST):
    """
    reçoit: une requête pour l'API de la MEL (str) avec une valeur par défaut si non précisé
    renvoi : datas renvoyées par l'API (dict)
    """
    with urllib.request.urlopen(request) as jsonfile:
        data = json.loads(jsonfile.read().decode())
    return(data)
    
def treatRequest(data):
    """
    reçoit: données extraites d'une requete à l'API (dict)
    retourne: données qui nous interessent* (data frame) 
    
    *à savoir: date_ech, valeur
    """
    listeDesRecords = data['records']
    listeDesFields = []
    for r in listeDesRecords: #on récupère chaque fields de données
        listeDesFields.append(r['fields']) 
    dico = []
    for k in listeDesFields:
        dico.append({'date' : k['date_ech'][0:10],'value' : k['valeur']})
    df = pd.DataFrame(dico)
    return(df)    
   
 
if __name__ == '__main__':
    data = getRequest()
    df = treatRequest(data)
    df.to_csv("data_MEL_API.csv", index=False,sep=';')
    
   