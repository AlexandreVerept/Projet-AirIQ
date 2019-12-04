import pandas as pd
import os

def resampleDataBeehive():
    os.chdir("datas/")
    
    df = pd.read_csv('DatasetRuche.csv',header=0,delimiter=';')
    df['time'] = pd.to_datetime(df['time'])
    df = df[["time","TempExt","HygroExt"]]
    df.index = df['time']

    # replace the NA by previous values
    df = df.fillna(method='ffill')
    
    # transform the dataset in homogenes measures (every 3 hours)    
    df = df.resample(rule='3H', base=0).mean()
    df = df.fillna(method='ffill')
    
    df["TempExt"] = df["TempExt"].map(arrondi)
    df["HygroExt"] = df["HygroExt"].map(arrondi)
    
    df.to_csv("DataISEN.csv",sep=';')
    
def arrondi(x):
    return(round(x,2))

resampleDataBeehive()