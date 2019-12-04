
import pandas as pd
import datetime

dfMel = pd.read_csv("datas/data_MEL_API.csv", header=0, delimiter=';')
dfBee = pd.read_csv("datas/DataISEN.csv", header=0, delimiter=';')

listeDataJours = []

for m in range(0,len(dfMel)):    
    b = dfMel.at[m,"date"]
    b = datetime.datetime.strptime(b, '%Y-%m-%d')
    b = b.date()
    print(b)
    for r in range(0,len(dfBee)):
        a = dfBee.at[r,"time"]
        a = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
        if b == a.date():
            try :
                listeDataJours.append({"Date" : str(a),
                                       "temperature" : dfBee.at[r,"TempExt"],
                                       "humidite" : dfBee.at[r,"HygroExt"],
                                       "IQ" : dfMel.at[m,"value"]})
            except:
                print("Error:",a.date())
        
print(len(listeDataJours))
df = pd.DataFrame(listeDataJours) 
df.to_csv("datas/testingDataset.csv", index=False,sep=';')
    