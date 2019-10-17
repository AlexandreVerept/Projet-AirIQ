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
    moyTempExt, moyHygroExt, moyPanneauS, moyBatterie, effectif = 0,0,0,0,0
    b = dfMel.at[m,"date"]
    b = datetime.datetime.strptime(b, '%Y-%m-%d')
    b = b.date()
    indexRuche = []
    for r in range(0,len(dfRuche)):
        a = dfRuche.at[r,"time"]
        a = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
        if b == a.date():
            moyTempExt+= dfRuche.at[r,"TempExt"]
            moyHygroExt+= dfRuche.at[r,"HygroExt"]
            moyPanneauS+= dfRuche.at[r,"PanneauS"]
            moyBatterie+= dfRuche.at[r,"Batterie"]
            effectif +=1
    if effectif != 0:
        listeDataJours.append({"Date" : b,
                               "TempExt": moyTempExt/effectif, 
                               "HygroExt" : moyHygroExt/effectif,
                               "PanneauS" : moyPanneauS/effectif,
                               "Batterie" : moyBatterie/effectif,
                               "IQ" : dfMel.at[m,"value"]})
print(len(listeDataJours))
df = pd.DataFrame(listeDataJours) 
df.to_csv("DataParJour.csv", index=False,sep=';')
    