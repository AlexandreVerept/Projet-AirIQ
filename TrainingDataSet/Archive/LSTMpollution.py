# source here: https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
# course here: https://machinelearningmastery.com/start-here/#timeseries

from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
 
# convert series to supervised learning
def series_to_supervised(data,n_in,n_out,n_out_plus1):

    df = DataFrame(data)
    cols, names = list(), list()
	
    for i in range(0,n_in):
        cols.append(df[i])
        name = "Var{}_(t-1)".format(i)
        names.append(name)
        
    for i in range(n_in,n_out+n_in):
        cols.append(df[i])
        name = "Var{}_(t)".format(i)
        names.append(name)
        
    for i in range(n_out+n_in,n_out+n_in+n_out_plus1):
        cols.append(df[i])
        name = "Var{}_(t+1)".format(i)
        names.append(name)
    
	# put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    agg.dropna(inplace=True)
    return agg
 
# load dataset
dataset = read_csv('Dataset.csv', header=0, delimiter=';', index_col=0)
values = dataset.values

# dislay our datas
#dataset.plot(subplots=True)
print(dataset.head())

# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 4, 1,1)
print(reframed.head())
 
# split into train and test sets
values = reframed.values
n_train_hours = int(len(dataset)*3/4)
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
 
# design network
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()
 
# make a prediction
yhat = model.predict(test_X)
rmse = sqrt(mean_squared_error(test_y, yhat))
print('Test RMSE: %.3f' % rmse)