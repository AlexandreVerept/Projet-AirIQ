"""
Ce script contient toutes les fonctions utiles à l'extraction 
des données et leur mise en forme pour le dataset
"""

import pandas as pd

DEFAULT_RUCHE_HEADER = ['Id','NumRuche','TempBoard','TempInt','HygorInt','Poids','TempExt','HygroExt','PanneauS','Batterie','time']

def extractCSV(CSVName,newCSVName,listOfColumns):
    """
    Select data we need in a CSV and return an other CSV file
    """
    df = pd.read_csv(CSVName+".csv", header=0, delimiter=';')[listOfColumns]
    df.to_csv(newCSVName+".csv", index=False)
    
def addHeaderCSV(CSVName,newCSVName,header = DEFAULT_RUCHE_HEADER):
    """
    Ajoute le header dans un CSV
    """
    df = pd.read_csv(CSVName+".csv", delimiter=',', names = header)
    df.to_csv(newCSVName+".csv", index=False,sep=';')
    

if __name__ == '__main__':
    #MEL
    myListMEL = ["date_ech","valeur"]
    extractCSV("indice-qualite-de-lair","DatasetMEL",myListMEL)
    
    #Ruche
    addHeaderCSV('RecuperationDonnees','DatasetRuche')
    myListRuche = ['TempExt','HygroExt','PanneauS','Batterie','time']
    extractCSV("DatasetRuche","DatasetRuche",myListRuche)
    
    