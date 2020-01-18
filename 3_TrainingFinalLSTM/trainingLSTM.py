import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import time
from sklearn.utils import shuffle

#=======================Parameters================================
LOAD = True # load model or create one
MODEL_TO_LOAD_NAME = 'model1576748233.5927076.h5'
PATH_TO_MODELS = "Models/"

TRAIN = False # train the model or not
EPOCHS = 1

features_considered = ['temperature','humidite','IQ','IQ_J+1']

#CSV_PATH = "CreateDataset/datas/testingDataset12.csv"
CSV_PATH = "CreateDataset/datas/trainingDatasetOffset12.csv"
#CSV_PATH = "CreateDataset/datas/testMix.csv"

NB_MEASURES = 8
SIZE_LSTM = 8

RANDOM_SHUFFLE_SEED = 0
#================================================================

# Importer dataset et voir les features

df = pd.read_csv(CSV_PATH, header=0, delimiter=';')

features = df[features_considered]
features.index = df['Date']

#normalize
features['temperature'] = features['temperature'].apply(lambda x: (x - (-12.30))/((46.90)-(-12.30)))
features['humidite'] = features['humidite'].apply(lambda x: x/100)
features['IQ'] = features['IQ'].apply(lambda x: x/10)

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
    y_train = chunks[:,0,-1]
    x_train,y_train = shuffle(x_train,y_train, random_state=RANDOM_SHUFFLE_SEED)
    return(x_train, y_train)
    
def kFold(x,y,k):
    """
    create what we need for cross validation
    """
    foldSize = int(len(x)/k)
    x_fold = []
    y_fold = []
    for i in range(k):
        x_fold.append(x[i*foldSize:(1+i)*foldSize])
        y_fold.append(y[i*foldSize:(1+i)*foldSize])
    return(x_fold,y_fold)    

# 1 jour = 96 mesures
x_train,y_train = createTraining(dataset,NB_MEASURES,len(features_considered)-1)
x_fold, y_fold = kFold(x_train,y_train,6)


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
    for i in range(len(x_fold)):
        x = []
        y = []
        for j in range(len(x_fold)):
            if i!=j:
                if len(x)>0:
                    x = np.concatenate([x,x_fold[j]],axis=0)
                    y = np.concatenate([y,y_fold[j]],axis=0)
                else:
                    x=x_fold[j]
                    y=y_fold[j]
                
        history = model.fit(x,
                            y,
                            epochs=EPOCHS,
                            steps_per_epoch=len(x_train))
    
    if len(history.history['loss'])>1:
        # plot history
        plt.plot(history.history['loss'], label='loss')
        plt.suptitle('Model training', fontsize=20)
        plt.xlabel('Epochs', fontsize=18)
        plt.ylabel('Loss', fontsize=16)
        plt.show()
    
    name = "model"+str(time.time())
    model.save(PATH_TO_MODELS+ name+".h5")


def calc_accuracy(y_pred,y_true):
    """
    calculate the accurracy of the prediction according to the true value
    """
    count=0
    for i in range(0,len(y_true)):
        if y_true[i]==round(y_pred[i][0]):
            count+=1
    if count==0:
        return(0)
    return(count/len(y_true)*100)
    
def mean_error(y_pred,y_true):
    """
    calculate the mean error between the prediction and the true value
    """
    total_error=0
    for i in range(0,len(y_true)):
        total_error += abs(y_true[i] - y_pred[i][0])
    return(total_error/len(y_true))

if TRAIN:
    #plot predict
    y_pred_train = model.predict(x_train)
    
    plt.plot(y_train, label='Real')
    plt.plot(y_pred_train, label='Prediction')
    plt.suptitle('Prediction of the air index quality (training data)', fontsize=20)
    plt.xlabel('Days', fontsize=18)
    plt.ylabel('IQ J+1', fontsize=16)
    plt.legend()
    plt.show()

    print("Accuracy with training data:", round(calc_accuracy(y_pred_train,y_train),2) ,"%")
    print("Mean error with training data:", round(mean_error(y_pred_train,y_train),2))

    """
    #plot predict
    y_pred_val = model.predict(x_val)

    plt.plot(y_val, label='Real')
    plt.plot(y_pred_val, label='Prediction')
    plt.suptitle('Prediction of the air index quality (validation data)', fontsize=20)
    plt.xlabel('Days', fontsize=18)
    plt.ylabel('IQ J+1', fontsize=16)
    plt.legend()
    plt.show()

    print("Accuracy with validation data:", round(calc_accuracy(y_pred_val,y_val),2) ,"%")
    print("Mean error with validation data:", round(mean_error(y_pred_val,y_val),2))
    """
else:
    #plot predict
    y_pred = model.predict(x_train)
    
    plt.plot(y_train, label='Real')
    plt.plot(y_pred, label='Prediction')
    plt.suptitle('Prediction of the air index quality', fontsize=20)
    plt.xlabel('Days', fontsize=18)
    plt.ylabel('IQ J+1', fontsize=16)
    plt.legend()
    plt.show()

    print("Accuracy:", round(calc_accuracy(y_pred,y_train),2) ,"%")
    print("Mean error:", round(mean_error(y_pred,y_train),2))
