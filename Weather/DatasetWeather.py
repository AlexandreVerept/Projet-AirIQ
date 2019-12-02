"""
Ce script récupère les CSV de weather et crée le csv que nous voulons
"""

import pandas as pd
import os

def importDataOfLille():
    #change directory
    os.chdir("datas/")
    filesList = os.listdir()
    
    dfList = []
    
    for filename in filesList:        
        df = pd.read_csv(filename, header=0, delimiter=';')
        
        #select data from Lille-Lesquin
        df = df.loc[df['numer_sta'] == 7015]
        #change datetime format
        df['date'] = pd.to_datetime(df['date'],format = '%Y%m%d%H%M%S')
        
        dfList.append(df)

    df = pd.concat(dfList, axis=0, ignore_index=True)
    
    df.to_csv("DataLilleWeather.csv", index=False,sep=';')
    

importDataOfLille()