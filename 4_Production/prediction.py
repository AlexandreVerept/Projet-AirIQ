import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

MODEL_NAME = "goodTest.h5"

def LSTM():
    features = pd.read_csv("datas/predictionData.csv", header=0, delimiter=';')
    print(features)
    features.index = features['Date']

    #normalize
    #normalize
    features['temperature'] = features['temperature'].apply(lambda x: (x - (-12.30))/((46.90)-(-12.30)))
    features['humidite'] = features['humidite'].apply(lambda x: x/100)
    features['IQ'] = features['IQ'].apply(lambda x: x/10)
    
    features.plot(subplots=True)
    plt.show()
    
    #reshape
    x = np.array(features)
    x = x[:,1:4]
    x = np.reshape(x,(1,8,3))    
    
    model = keras.models.load_model("LSTM_model/"+MODEL_NAME)
    model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')
    
    y_pred= model.predict(x)[0,0]
    return(y_pred)