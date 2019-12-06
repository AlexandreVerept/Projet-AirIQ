import pandas as pd


def offset():

    df = pd.read_csv('datas/trainingDataset.csv',header=0,delimiter=';')
    
    df['temperature'] = df['temperature'].apply(lambda x: round(x + 2.22,2))
    
    df.to_csv("datas/trainingDatasetOffset.csv", index = False, sep=';')
    

offset()