# -*- coding:utf-8 -*-
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

with open('movie.json', 'r', encoding='utf-8') as myFile:
    data = json.load(myFile)
    # json --> dict type(사전 자료형)
print(data)

font_name = fm.FontProperties(fname='c:/Windows/Fonts/H2GTRM.ttf').get_name()
rc('font', family=font_name)

dataPie = [float(i['book']) for i in data['movie']]
print(dataPie)
plt.pie(dataPie)

category = [i['title'] for i in data['movie']]
print(category)

plt.legend(category)

plt.show()
