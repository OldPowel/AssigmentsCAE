import os
import pandas
import numpy as np
import threading
from pprint import pprint
import matplotlib.pyplot as plt


def ploting (fft_t, fft_sig):
   plt.figure()
   plt.stem(np.fft.fftshift(fft_f), np.fft.fftshift(np.abs(fft_sig)))
   plt.show()




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

dt = daten[file]['t(s)'][2]-daten[file]['t(s)'][1]

fft_f = np.fft.fftfreq(len(daten[file]['t(s)']), dt)
fft_sig = np.fft.fft(daten[file]['y(m)']) * dt

thread1 = threading.Thread( target = ploting, args = (fft_f, fft_sig) )
thread1.start()
thread1.join()
