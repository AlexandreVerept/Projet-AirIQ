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
#data = data.drop(data.index[-150:])

plt.title("Temperature")

plt.plot(data['temperatureRuche'],label='Ruche')
plt.plot(data['temperatureMeteo'],label='Meteo')

plt.xlabel('Measures')
plt.ylabel('°C')
plt.legend()
plt.show()

#===============
#temperature difference
#===============
diffTemp = data['temperatureRuche']-data['temperatureMeteo']
txt = "Mean = "+str(round(diffTemp.mean(axis=0),2))+" ; Standard deviation: "+str(round(diffTemp.std(axis=0),2))

plt.title("Temperature difference (Beehive - Meteo France)\n"+txt)

plt.plot(diffTemp, label ="difference", color ='lightgreen')

plt.xlabel('Measures')
plt.ylabel('delta °C')
plt.show()


#===============
#humidity
#===============

plt.title("Humidity")
plt.plot (data['humiditeMeteo'],label='Meteo')
plt.plot (data['humiditeRuche'],label='Ruche')

plt.xlabel('Measures')
plt.ylabel('humidity %')
plt.legend()
plt.show()

#===============
#humidity difference
#===============
diffHum = data['humiditeRuche']-data['humiditeMeteo']

txt = "Mean = "+str(round(diffHum.mean(axis=0),2))+" ; Standard deviation: "+str(round(diffHum.std(axis=0),2))

plt.title("Humidity difference (Beehive - Meteo France)\n"+txt)

plt.plot(diffHum, label ="difference", color ='lightgreen')

plt.xlabel('Measures')
plt.ylabel('delta humidity %')
plt.show()
