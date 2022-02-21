# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:28:36 2021

@author: srpdo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm




data_0 =  np.loadtxt("data2.txt")


hist_data = []                  #will hold datas for histograms


for i in range(len(data_0[0])):  #create as many arrays as collums in the data
    hist_data.append([])
    
    
for i in range(len(data_0)):            #fills the main data array with every column of data given as an array
    for j in range(len(data_0[0])):
        hist_data[j].append(data_0[i][j])
        

titles = ["mt1", "mt2", "fin", "lab", "hw", "Att."]



figure,axis = plt.subplots(2,3)         #creates a canvas for each graph, 2 rows and 3 columns



for i in range(len(titles)):        #creates as many graphs as the number of titles
    x = 0 if i < 3 else 1           #first 3 graph will be drawn on the first row
    y = i if i < 3 else i-3         #rows will go as 1-2-3-1-2-3
    axis[x,y].set_title(titles[i])

    _, bins, _ = axis[x,y].hist(hist_data[i], 10, density=1, alpha=1) 
    mu,sigma = norm.fit(hist_data[i])                                      #calculates the mean and standart deviation for each column

    best_fit_line = norm.pdf(bins, mu, sigma)                           #line of gaussian dist.   
    axis[x,y].plot(bins, best_fit_line)                                 #plot the fit for every fig.



plt.show()
