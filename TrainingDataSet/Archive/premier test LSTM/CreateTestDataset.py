"""
Ce script récupère les CSV de la MEL et la Ruche directement après 
avoir été récupérées par l'API et traitées
"""

import pandas as pd
import datetime

dfMel = pd.read_csv("data_MEL_API.csv", header=0, delimiter=';')
dfRuche = pd.read_csv("DatasetRuche.csv", header=0, delimiter=';')

listeDataJours = []
for m in range(0,len(dfMel)): 
    moyTempExt, moyHygroExt, moyPanneauS, moyBatterie = 0,0,0,0
    b = dfMel.at[m,"date"]
    b = datetime.datetime.strptime(b, '%Y-%m-%d')
    b = b.date()
    indexRuche = []
    for r in range(0,len(dfRuche)):
        a = dfRuche.at[r,"time"]
        a = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
        if b == a.date():
            try :
                listeDataJours.append({"Date" : b,
                                       "Heure" : a.time(),
                                       "TempExt": dfRuche.at[r,"TempExt"], 
                                       "HygroExt" : dfRuche.at[r,"HygroExt"],
                                       "PanneauS" : dfRuche.at[r,"PanneauS"],
                                       "Batterie" : dfRuche.at[r,"Batterie"],
                                       "IQ" : dfMel.at[m,"value"],
                                       "IQ_j+1" : dfMel.at[m-1,"value"]})
            except:
                print("Error:",a.date())
print(len(listeDataJours))
df = pd.DataFrame(listeDataJours) 
df.to_csv("Dataset.csv", index=False,sep=';')
    