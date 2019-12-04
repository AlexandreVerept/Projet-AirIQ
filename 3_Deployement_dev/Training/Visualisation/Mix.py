# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:31:31 2019

@author: maxou
"""

import pandas as pd
import datetime

dataISEN = pd.read_csv("datas/DataISEN.csv", header=0, delimiter=';')
trainingDataset = pd.read_csv("datas/trainingDataset.csv", header=0, delimiter=';')

listeDataJours = []

for m in range(0,len(dataISEN)):    
    b = dataISEN.at[m,"time"]
    b = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
    for r in range(0,len(trainingDataset)):
        a = trainingDataset.at[r,"Date"]
        a = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
        if b == a:
            try :
                listeDataJours.append({"Date" : str(a),
                                       "temperatureMeteo" : trainingDataset.at[r,"temperature"],
                                       "humiditeMeteo" : trainingDataset.at[r,"humidite"],
                                       "temperatureRuche" : dataISEN.at[m,"TempExt"],
                                       "humiditeRuche" : dataISEN.at[m,"HygroExt"]
                                       })
            except:
                print("Error:",a)
                
print(len(listeDataJours))            
df = pd.DataFrame(listeDataJours) 
df.to_csv("datas/affichagePourGrapheTemp.csv", index=False,sep=';')