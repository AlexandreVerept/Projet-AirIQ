import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import time

from sklearn.utils import shuffle

#=======================Parameters================================
LOAD = False # load model or create one
MODEL_TO_LOAD_NAME = 'modelNew.h5'
PATH_TO_MODELS = "Models/"

TRAIN = True # train the model or not
EPOCHS = 10

features_considered = ['PanneauS', 'TempExt','HygroExt','IQ','IQ_j+1']
features_to_normalize = ['PanneauS', 'TempExt','HygroExt']

NB_MEASURES = 96
SIZE_LSTM = NB_MEASURES

RANDOM_SHUFFLE_SEED = 0
#================================================================

# Importer dataset et voir les features

df = pd.read_csv("Dataset.csv", header=0, delimiter=';')

features = df[features_considered]
features.index = df['Date']

#normalize
f = features[features_to_normalize]
features[features_to_normalize] = (f-f.min())/(f.max()-f.min())

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
    x_train = chunks[:,:,0:index_features_in]
    y_train = chunks[:,-1,-1]
    x_train,y_train = shuffle(x_train,y_train, random_state=RANDOM_SHUFFLE_SEED)
    return(x_train, y_train)    
    
def calc_accuracy(y_pred,y_val):
    count=0
    for i in range(0,len(y_val)):
        if y_val[i]==round(y_pred[i][0]):
            count+=1
    if count==0:
        return(0)
    return(count/len(y_val)*100)

# 1 jour = 96 mesures
x_train,y_train = createTraining(dataset,NB_MEASURES,len(features_considered)-1)

#split pour validation
split = int(len(y_train)*5/6)

x_val = x_train[split:-1]
x_train = x_train[0:split]

y_val = y_train[split:-1]
y_train = y_train[0:split]

# Load the model or create it
if LOAD: 
    model = keras.models.load_model(PATH_TO_MODELS + MODEL_TO_LOAD_NAME)
    model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')
else:
    # Model
    input_shape = (x_train.shape[-2],x_train.shape[-1])

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.LSTM(SIZE_LSTM,input_shape=input_shape,name='LSTM_layer',go_backwards=True))
    model.add(tf.keras.layers.Dense(1,name="Dense_layer"))
    model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')
    model.summary()

if TRAIN:
    # Train  
    history = model.fit(x_train,
                        y_train,
                        epochs=EPOCHS,
                        steps_per_epoch=len(x_train))
    
    if len(history.history['loss'])>1:
        # plot history
        plt.plot(history.history['loss'], label='loss')
        plt.suptitle('Model training', fontsize=20)
        plt.xlabel('Epochs', fontsize=18)
        plt.ylabel('Loss', fontsize=16)
        plt.show()
        
    model.save(PATH_TO_MODELS+"model"+str(time.time())+".h5")

#plot predict
y_pred = model.predict(x_train)
    
plt.plot(y_train, label='Real')
plt.plot(y_pred, label='Prediction')
plt.suptitle('Prediction of the air index quality', fontsize=20)
plt.xlabel('Days', fontsize=18)
plt.ylabel('IQ', fontsize=16)
plt.legend()
plt.show()

print("Accuracy:", calc_accuracy(y_pred,y_val))