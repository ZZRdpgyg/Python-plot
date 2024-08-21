# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:44:02 2023

@author: Zirui Zhang
"""

from pandas import *
import matplotlib.pyplot as plt
import csv
import numpy as np
f = open('./cons_inco_data.csv', 'r')
line = [0,0,0,0,0,0,0,0,0,0,0,0]
line_ = [0,1,2,3,4,5,6,7,8,9,10,11]
yline = [-0.6,0.6]
xline = [4,4]
data_point = [0.2,1,2,3,4,5,6,7,8,9]
data = read_csv('./cons_inco_data.csv') 
cons = data['cons'].tolist()
inco = data['inco'].tolist()
target = data['target'].tolist()

c_err = data['cons_SE']
i_err = data['inco_SE']
tar_err = data['tar_SE']

inco_cons = []
cons_tar = []
inco_tar = []

intar_contar = []

for i,j in zip(inco,cons):
    c = i - j
    inco_cons.append(c)

for i,j in zip(inco,target):
    c = i -j
    inco_tar.append(c)
for i,j in zip(cons,target):
    c = i-j
    cons_tar.append(c)

for i,j in zip(inco_tar,cons_tar):
    c = i - j
    intar_contar.append(c)

fd, ax = plt.subplots()
#plt.plot(xline, yline,'-', color = 'black', linewidth = 0.4)
#plt.plot(line_, line,'--', color = 'black', linewidth= 1)
#plt.plot(data_point, inco_cons,'o-',label = 'inconsistent-consistent',color = 'green')
#plt.plot(data_point, inco_tar,'o-',label = 'inconsistent-target',color = 'red')
#plt.plot(data_point, cons_tar,'o-',label = 'consistent-target', color = 'orange')
#plt.plot(data_point, intar_contar,'o-',label = 'inco_tar - cons_target', color = 'blue')

ax.errorbar(data_point,inco,yerr=i_err,fmt='-',color = 'seagreen',label = 'inconsistent',linewidth=4)
ax.errorbar(data_point,cons,fmt='-',yerr=c_err,color = 'brown', label = 'consistent',linewidth=4)
ax.errorbar(data_point,target,fmt='-',yerr=tar_err,color = 'grey', label = 'target',linewidth=4)



ax.legend(loc='upper right',frameon=False)
#ax.set_axis_off() # remove the axis
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xlim([0,11])
plt.ylim([-0.6,0.6])

plt.xlabel('Deconvoluntion data points')
plt.ylabel('Beta weights')


plt.title('Average V1 responses')
#plt.title('difference')


plt.show()
    
    




