import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import LSTM
#from keras.optimizers import Adam
import pandas as pd
import numpy as np

dataIn = pd.read_csv("Dataset.csv", header=0, delimiter=';')[["Batterie","HygroExt","PanneauS","TempExt","IQ"]].to_numpy()
dataOut = pd.read_csv("Dataset.csv", header=0, delimiter=';')[["IQ_j+1"]].to_numpy()

(r,featuresSize) = np.shape(dataIn)
(r,labelSize) = np.shape(dataOut)

print(np.shape(dataIn))
print(np.shape(dataOut))

arrayIn = dataIn.reshape(len(dataIn),1,featuresSize)
arrayOut = dataOut.reshape(len(dataOut),1,labelSize)

model = Sequential()

# shape keras (batch_size, time_steps, seq_len)

model.add(LSTM(100,batch_input_shape=np.shape(arrayIn),activation='sigmoid',return_sequences=False,name="LSTM_layer"))
#model.add(Dropout(0.2))
model.add(Dense(1,name="Dense_Layer"))

#opt = Adam(lr=1e-3, decay=1e-5)
model.compile(loss='sparse_categorical_crossentropy', optimizer="Adam", metrics=['accuracy'])

print(model.summary())

model.fit(arrayIn,arrayOut, epochs=1)
print("oui!!!")
lol = model.predict([arrayIn])