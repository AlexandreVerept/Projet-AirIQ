# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:08:02 2019

@author: maxou
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("datas/affichagePourGrapheTemp.csv", header=0, delimiter=';')

#===============
#temperature
#===============

plt.title("Temperature")

plt.plot(data['temperatureRuche'],label='Ruche')
plt.plot(data['temperatureMeteo'],label='Meteo')

plt.xlabel('Days')
plt.ylabel('°C')
plt.legend()
plt.show()

#===============
#temperature difference
#===============

plt.title("Temperature difference (Ruche - Meteo)")
diffTemp = data['temperatureRuche']-data['temperatureMeteo']
plt.plot(diffTemp, label ="difference", color ='lightgreen')

plt.xlabel('Days')
plt.ylabel('delta °C')
plt.show()
print("Mean = ",round(diffTemp.mean(axis=0),2)," ; Standard deviation: ",round(diffTemp.std(axis=0),2))

#===============
#humidity
#===============

plt.title("Humidity")
plt.plot (data['humiditeMeteo'],label='Meteo')
plt.plot (data['humiditeRuche'],label='Ruche')

plt.xlabel('Days')
plt.ylabel('humidity %')
plt.legend()
plt.show()

#===============
#humidity difference
#===============

plt.title("Humidity difference (Ruche - Meteo)")
diffHum = data['humiditeRuche']-data['humiditeMeteo']
plt.plot(diffHum, label ="difference", color ='lightgreen')

plt.xlabel('Days')
plt.ylabel('delta humidity %')
plt.show()
print("Mean = ",round(diffHum.mean(axis=0),2)," ; Standard deviation: ",round(diffHum.std(axis=0),2))