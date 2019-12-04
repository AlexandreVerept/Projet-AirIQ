import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

MODEL_NAME = "10epochs.h5"

def LSTM():
    features = pd.read_csv("datas/predictionData.csv", header=0, delimiter=';')
    features.index = features['Date']

    #normalize
    features_to_normalize = ['temperature','humidite']
    f = features[features_to_normalize]
    features[features_to_normalize] = (f-f.min())/(f.max()-f.min())

    print(features.head())
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