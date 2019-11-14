import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

# Importer dataset et voir les features

df = pd.read_csv("Dataset.csv", header=0, delimiter=';')

features_considered = ['PanneauS', 'TempExt','HygroExt','IQ','IQ_j+1']
features = df[features_considered]
features.index = df['Date']

print(features.head())
features.plot(subplots=True)
plt.show()

# On normalise :
dataset = features.values
"""
data_mean = dataset.mean(axis=0)
data_std = dataset.std(axis=0)

dataset = (dataset-data_mean)/data_std"""

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

# Model

input_shape = (x_train.shape[-2],x_train.shape[-1])

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.LSTM(96,input_shape=input_shape,name='LSTM_layer'))
model.add(tf.keras.layers.Dense(1,name="Dense_layer"))
model.compile(optimizer=tf.train.RMSPropOptimizer(learning_rate=0.005), loss='mae')

# Train
EPOCHS = 10
EVALUATION_INTERVAL = 131

history = model.fit(x_train,
                    y_train,
                    epochs=EPOCHS,
                    steps_per_epoch=EVALUATION_INTERVAL)

# plot history
plt.plot(history.history['loss'], label='loss')
plt.legend()
plt.show()

#plot predict
plt.plot(y_train, label='Real')
plt.plot(model.predict(x_train), label='Prediction')
plt.legend()
plt.show()
