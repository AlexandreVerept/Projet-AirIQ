"""
Script routine qui s'occupe d'appeler les autres scripts necessaires 
au bon fonctionnement du projet AirIQ
"""
import schedule
import time

#personnal librairies
import datasUtilities as du
import prediction as pre

ERROR_NUMBER = 0

def call_script():
    """
    Fonction qui appelle les scripts
    """
    
    print("Lancement des scripts...")
    # get the datas up to date:
    global ERROR_NUMBER
    ERROR_NUMBER = 0
    if launch(du.collectDatasFromTheDatabase):
        if launch(du.collectTheAirIQ):
            if launch(du.mixIQandRuche):
                print("Succes de la creation des datasets")    
                #make the prediction
                if launch(pre.lstm):
                    print("Succes de la prediction")
    
def launch(function):
    """
    Lance une fonction, et la relance a intervalle regulier. 
    Aubout d'un certain nombre d'echecs, la fonction retourne faux
    
    @return: True si tout a bien fonctionne, False sinon
    """
    global ERROR_NUMBER
    check = False
    while not check:
        try:
            check = function()
        except:
            check = False
        if not check:
            ERROR_NUMBER += 1            
            if ERROR_NUMBER > 5:
                print("Abandon du script, veuillez verifier que tout va bien (arborescence, connexion, ruche...)")
                return(False)
            time.sleep(30)
    return(True)

if __name__ == '__main__':
    # Appelle la fonction call script qui va appeler le script python tous les jours
    
    schedule.every().day.at('12:00').do(call_script)
    #schedule.every(1).minutes.do(call_script)

    # Boucle infinie afin de pouvoir appeler la fonction au moment predefini 
    while True:
        schedule.run_pending()
        time.sleep(60)