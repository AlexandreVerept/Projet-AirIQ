# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:08:02 2019

@author: maxou
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("datas/affichagePourGrapheTemp.csv", header=0, delimiter=';')

#temps
plt.title("Temperature")
plt.plot (data['temperatureMeteo'],label='Meteo')
plt.plot (data['temperatureRuche'],label='Ruche')

plt.show()

plt.title("Temperature difference")
plt.plot(data['temperatureRuche']-data['temperatureMeteo'], label ="difference")

plt.show()

#hum
plt.title("Humidite")
plt.plot (data['humiditeMeteo'],label='Meteo')
plt.plot (data['humiditeRuche'],label='Ruche')

plt.show()

plt.title("Humidite difference")
plt.plot(data['humiditeRuche']-data['humiditeMeteo'], label ="difference")

plt.show()