import pandas as pd
import os

os.chdir("datas/")

def cleanDataLille():
    df = pd.read_csv('DataLilleWeather.csv',header=0,delimiter=';')
    df['date'] = pd.to_datetime(df['date'])
    df = df[["date","t","u"]]
    df.index = df["date"]    
   
    liste_columns_to_clean = ["t","u"]
    
    for column in liste_columns_to_clean:
        df[column] = df[column].map(erase_mq)
        
    # replace the NA by previous values
    df = df.fillna(method='ffill')
    
    df["t"] = df["t"].map(conversionTemperature)
      
    df.to_csv("DataLilleClean1996_2019.csv", index=False,sep=';')
    
def conversionTemperature(x):
    return(round(x - 273.15,3))
    
def erase_mq(x):
    if x == "mq":
        x = None
    else:
        x = float(x)
    return(x)       

    
cleanDataLille()