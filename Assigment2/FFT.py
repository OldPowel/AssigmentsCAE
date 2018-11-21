import os
import pandas
from pprint import pprint

verzeichnis = 'histDatein'

files = os.listdir(verzeichnis)

# pprint(files)

file = files[1]

daten = {}
for file in files:
   if file.find('.hist') != 0:
      tmp = pandas.read_csv(verzeichnis + '/' + file, skiprows=[0, 1, 2, 3, 4, 5, 6, 7], header=None, sep=' ')
      daten[file] = {'t(s)': tmp[0].tolist()}
      daten[file]['x(m)'] = tmp[2].tolist()
      daten[file]['y(m)'] = tmp[4].tolist()

# 
# print(daten)
