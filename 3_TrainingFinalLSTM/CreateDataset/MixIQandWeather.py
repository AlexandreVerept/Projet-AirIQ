
import pandas as pd
import datetime

dfMel = pd.read_csv("datas/data_MEL_API.csv", header=0, delimiter=';')
dfWeather = pd.read_csv("datas/DataLilleClean1996_2019.csv", header=0, delimiter=';')

listeDataJours = []

for m in range(0,len(dfMel)):    
    b = dfMel.at[m,"date"]
    b = datetime.datetime.strptime(b, '%Y-%m-%d')
    b = b.date()
    print(b)
    for r in range(0,len(dfWeather)):
        a = dfWeather.at[r,"date"]
        a = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
        if b == a.date():
            try :
                listeDataJours.append({"Date" : str(a),
                                       "temperature" : dfWeather.at[r,"t"],
                                       "humidite" : dfWeather.at[r,"u"],
                                       "IQ" : dfMel.at[m,"value"],
                                       "IQ_J+1" : dfMel.at[m-1,"value"]})
            except:
                print("Error:",a.date())
        
print(len(listeDataJours))
df = pd.DataFrame(listeDataJours) 
df.to_csv("datas/trainingDataset.csv", index=False,sep=';')
    