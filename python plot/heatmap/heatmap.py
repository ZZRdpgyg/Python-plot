# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:42:17 2023

@author: ziruiz
"""

import csv
import matplotlib.pyplot as plt 
from pandas import *
import numpy as np

path = './'
f = open(path + 'office_score.txt','r')
c = open(path + 'office_name.txt','r')
data = read_csv(path + 'office_score.txt') 
daname = read_csv(path + 'office_name.txt') 
sscore = data['office'].tolist()
name = daname['name'].tolist()

test_score = []
for i in sscore:
    if i != 1.0:
        test_score.append(i)

atscore = np.array(test_score) #calculate the max mean median min value
print('max', np.max(atscore))
print('med',np.median(atscore))
print('mean', np.mean(atscore))
print('min', np.min(atscore))


hdata = np.array(sscore)
heat_data = np.reshape(hdata, (len(name),len(name))) #store them in an array

np.savetxt(path + 'office_similarity_array.csv',heat_data,delimiter=',')



fig, ax = plt.subplots()

im = ax.imshow(heat_data)
ax.set_xticks(np.arange(len(name)), labels=name, fontsize = 30)
ax.set_yticks(np.arange(len(name)), labels=name, fontsize = 30)
plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.80)
cbar.ax.set_ylabel('similarity', rotation=-90, va="bottom", fontsize = 70)
ax.set_title('Office Similarity', fontsize = 70)
fig.set_size_inches(35, 35, forward=True)
fig.savefig('Office_similarity.jpg', dpi=300)
plt.show()