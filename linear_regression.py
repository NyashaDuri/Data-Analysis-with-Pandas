#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# load the flights dataset
flights = pd.read_csv('flights.csv', index_col=False)
flights_subsample = flights.sample(1000)

# plot the data
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
plt.show()

# perform linear regression
slope, intercept, r_value, _, _ = linregress(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
print('y = {}x + {}; r={}'.format(slope, intercept, r_value))

# plot the data (again)
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])

# generate some X values to feed into the line
x = np.linspace(flights_subsample['DISTANCE'].min(), flights_subsample['DISTANCE'].max(), 1000)
# calculate the y values using the learned slope and intercept
y = slope * x + intercept
plt.plot(x, y, 'r--')
plt.show()

# use learned slope and intercept for prediction:
distance = 5000
flight_time = slope * distance + intercept
print(flight_time)
