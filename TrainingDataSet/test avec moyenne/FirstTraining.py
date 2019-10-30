"""
Ce script est un premier test de ML basé sur la moyenne des valeurs 
retournées chaque jour par les ruches
"""
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
#from keras.layers import Dropout
#from keras.callbacks import ModelCheckpoint
#from keras.utils import np_utils
from keras.optimizers import Adam

import pandas as pd
import tensorflow as tf

dataIn = pd.read_csv("DataParJour.csv", header=0, delimiter=';')[["Batterie","HygroExt","PanneauS","TempExt"]]
dataOut = pd.read_csv("DataParJour.csv", header=0, delimiter=';')[["IQ"]]

vectorIn = tf.constant(dataIn, shape=[139,4])
vectorOut = tf.constant(dataOut, shape=[139,1])

model = Sequential()
model.add(Dense(32, input_dim=4, activation='sigmoid'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='relu'))

opt = Adam(lr=0.001,)
model.compile(loss='mean_squared_error', optimizer=opt)

history = model.fit(dataIn,dataOut, epochs=100)

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

