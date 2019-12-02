import pandas as pd
import os

os.chdir("datas/")

def cleanDataLille():
    df = pd.read_csv('DataLilleWeather.csv',header=0,delimiter=';')
    df['date'] = pd.to_datetime(df['date'])
    df = df[["date","pmer","dd","ff","t","u","pres"]]
    df.index = df["date"]    
   
    liste_columns_to_clean = ["pmer","dd","ff","t","u","pres"]
    
    for column in liste_columns_to_clean:
        df[column] = df[column].map(erase_mq)
        
    # replace the NA by previous values
    df = df.fillna(method='ffill')
    
    df.to_csv("DataLilleWeatherClean.csv", index=False,sep=';')
    
def erase_mq(x):
    if x == "mq":
        x = None
    else:
        x = float(x)
    return(x)       

    
cleanDataLille()