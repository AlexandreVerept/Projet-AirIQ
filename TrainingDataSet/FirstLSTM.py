import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import time

#=======================Parameters================================
LOAD = True # load model or create one
MODEL_TO_LOAD_NAME = 'model1573734824.6870413.h5'
PATH_TO_MODELS = "Models/"

TRAIN = True # train the model or not
EPOCHS = 5
#================================================================

# Importer dataset et voir les features

df = pd.read_csv("Dataset.csv", header=0, delimiter=';')

features_considered = ['PanneauS', 'TempExt','HygroExt','IQ','IQ_j+1']
features = df[features_considered]
features.index = df['Date']

print(features.head())
features.plot(subplots=True)
plt.show()

# On charge les features interessantes :
dataset = features.values

# On crée le set d'entrainement:

def createTraining(dataset,nb_measures,index_features_in):
    # on va decouper le dataset en tranches de nb_measures:
    chunks = [dataset[x:x+nb_measures] for x in range(0, len(dataset), nb_measures)]
    del chunks[-1] # ddelete the last one as it may be inferior to nb_measures
    chunks = np.array(chunks) 
    print ("dataset shape:",chunks.shape)    
    x_train = chunks[:,:,0:index_features_in]
    y_train = chunks[:,-1,4]
    print ("train input shape:",x_train.shape)
    print ("train output shape:",y_train.shape)   
    return(x_train, y_train)

# 1 jour = 96 mesures
x_train,y_train = createTraining(dataset,96,4)

# Load the model or create it
if LOAD: 
    model = keras.models.load_model(PATH_TO_MODELS + MODEL_TO_LOAD_NAME)
    model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')
else:
    # Model
    input_shape = (x_train.shape[-2],x_train.shape[-1])

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.LSTM(96,input_shape=input_shape,name='LSTM_layer'))
    model.add(tf.keras.layers.Dense(1,name="Dense_layer"))
    model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')

if TRAIN:
    # Train    
    EVALUATION_INTERVAL = 100

    history = model.fit(x_train,
                        y_train,
                        epochs=EPOCHS,
                        steps_per_epoch=EVALUATION_INTERVAL)
    
    if len(history.history['loss'])>1:
        # plot history
        plt.plot(history.history['loss'], label='loss')
        plt.suptitle('Model training', fontsize=20)
        plt.xlabel('Epochs', fontsize=18)
        plt.ylabel('Loss', fontsize=16)
        plt.show()
        
    model.save(PATH_TO_MODELS+"model"+str(time.time())+".h5")

#plot predict
plt.plot(y_train, label='Real')
plt.plot(model.predict(x_train), label='Prediction')
plt.suptitle('Prediction of the air index quality', fontsize=20)
plt.xlabel('Days', fontsize=18)
plt.ylabel('IQ', fontsize=16)
plt.legend()
plt.show()


