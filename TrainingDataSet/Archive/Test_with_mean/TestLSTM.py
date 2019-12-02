import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM 
import pandas as pd
import numpy as np

dataIn = pd.read_csv("DataParJour.csv", header=0, delimiter=';')[["Batterie","HygroExt","PanneauS","TempExt"]].to_numpy()
dataOut = pd.read_csv("DataParJour.csv", header=0, delimiter=';')[["IQ"]].to_numpy()

(r,featuresSize) = np.shape(dataIn)
(r,labelSize) = np.shape(dataOut)

arrayIn = dataIn.reshape(len(dataIn),1,featuresSize)
arrayOut = dataOut.reshape(len(dataOut),1,labelSize)

model = Sequential()

model.add(LSTM(100,input_shape=(1,featuresSize),activation='sigmoid'))
#model.add(Dropout(0.2))

#model.add(Dense(32, activation='relu'))
model.add(Dense(1))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)
model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit(arrayIn,arrayOut, epochs=1)

lol = model.predict([arrayIn])