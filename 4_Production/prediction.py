import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

#personnal librairies
import datasUtilities as du

MODEL_NAME = "goodTest.h5"

def lstm():
    """
    Fonction qui effectue la prédiction de qualité de l'air, sur la base 
    des .csv fournis
    
    @return: True si tout a bien fonctionné, False sinon
    """
    try:
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
    except:
        print("ERREUR LORS DE L'IMPORT DE DONNEES DANS LA LSTM !")
        return(False)
    
    try:
        #reshape
        x = np.array(features)
        x = x[:,1:4]
        x = np.reshape(x,(1,8,3))    
    
        model = keras.models.load_model("LSTM_model/"+MODEL_NAME)
        model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')
    except:
        print("ERREUR LORS DE L'IMPORTATION DU MODEL DANS LA LSTM !")
        return(False)
        
    try:
        y_pred= model.predict(x)[0,0]    
        print("L'indice de qualite de l'air de demain :",y_pred)         
    except:
        print("ERREUR LORS DE LA PREDICTION DANS LA LSTM !")
        return(False)
        
    try:
        check = du.savePrediction(y_pred)
    except:
        check = False
    return(check)    
