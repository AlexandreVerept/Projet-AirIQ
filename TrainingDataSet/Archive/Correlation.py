from pandas import read_csv
from pandas import DataFrame
import matplotlib.pyplot as plt


dataset = read_csv('Dataset.csv', header=0, delimiter=';', index_col=0)
print(dataset.head())

for i in range(0,len(list(dataset))-2):
    plt.scatter(dataset[list(dataset)[i]], dataset["IQ"])
    plt.title("Correlation avec "+list(dataset)[i])
    plt.show()