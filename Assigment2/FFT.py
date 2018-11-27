import os
import pandas
import numpy as np
import threading
import time
from pprint import pprint
import matplotlib.pyplot as plt


def ploting (fft_t, fft_sig):
   plt.figure()
   plt.stem(np.fft.fftshift(fft_t), np.fft.fftshift(np.abs(fft_sig)))
   plt.show()
   # fig, ax = plt.subplots()
   # ax.plot(np.fft.fftshift(fft_t), np.fft.fftshift(np.abs(fft_sig))))
   # plt.show()




verzeichnis = 'histDatein'

files = os.listdir(verzeichnis)

# pprint(files)

# file = files[1]

daten = {}
for file in files:
   if file.find('.hist') != 0:
      tmp = pandas.read_csv(verzeichnis + '/' + file, skiprows=[0, 1, 2, 3, 4, 5, 6, 7], header=None, sep=' ')
      daten[file] = {'t(s)': tmp[0].tolist()}
      daten[file]['x(m)'] = tmp[2].tolist()
      daten[file]['y(m)'] = tmp[4].tolist()

legende=[]
j=1
#legendeneinträge
for file in files:
   number = file.find('-')
   legende.append(file[:number] )
   j +=1

dt = {}
fft_f = {}
fft_sig = {}

for file in files:
   dt[file] = daten[file]['t(s)'][2]-daten[file]['t(s)'][1]

   fft_f[file] = np.fft.fftfreq(len(daten[file]['t(s)']), dt[file])
   fft_sig[file] = np.fft.fft(daten[file]['y(m)']) * dt[file]

for file in files:
   falscheElemente = []
   for index, element in enumerate(fft_f[file]):
      if element < -1 or element > 200:
         falscheElemente.append(index)

   fft_f[file] = np.delete(fft_f[file], falscheElemente) 
   fft_sig[file] = np.delete(fft_sig[file], falscheElemente)

f=plt.figure()
i = 0
color=['ro', 'bo', 'go', 'co', 'yo']
color2=['r', 'b', 'g', 'c', 'y']

for file in files:
   plt.plot(fft_f[file], np.abs(fft_sig[file].real))
   #plt.stem(fft_f[file], np.abs(fft_sig[file]), color2[i], markerfmt=color[i], label=file)
   i += 1

plt.legend(legende)

plt.xlabel('Frequenz in Hz')
plt.ylabel('Delta y in m')
plt.grid(b=True, which = 'both')
plt.show()

f.savefig("TransientAnalysis.pdf")

# print('test')
# while 1:
#    time.sleep(3)
