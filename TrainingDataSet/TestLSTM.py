import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM 
import pandas as pd

dataIn = pd.read_csv("DataParJour.csv", header=0, delimiter=';')[["Batterie","HygroExt","PanneauS","TempExt"]].to_numpy()
dataOut = pd.read_csv("DataParJour.csv", header=0, delimiter=';')[["IQ"]].to_numpy()

arrayIn = dataIn.reshape(1,len(dataIn),4)
arrayOut = dataOut.reshape(1,len(dataIn),1)

model = Sequential()

model.add(LSTM(100, activation='sigmoid', return_sequences=False))
#model.add(Dropout(0.2))

#model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='relu'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)
model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit(arrayIn,arrayOut, epochs=1)

lol = model.predict([arrayIn])