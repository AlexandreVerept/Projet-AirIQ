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

plt.title("Temperature difference")
plt.plot(data['temperatureRuche']-data['temperatureMeteo'], label ="difference", color ='lightgreen')

plt.xlabel('Days')
plt.ylabel('delta °C')
plt.show()

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

plt.title("Humidity difference")
plt.plot(data['humiditeRuche']-data['humiditeMeteo'], label ="difference", color ='lightgreen')

plt.xlabel('Days')
plt.ylabel('delta humidity %')
plt.show()