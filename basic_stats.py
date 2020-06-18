#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

# load the flights dataset
#flights = pd.read_csv('flights.csv', index_col=False)

# get basic statistics for the dataframe
#print(flights.describe())

# compute the mean and standard deviation for a the DISTANCE column
#print(flights['DISTANCE'].mean())
#print(flights['DISTANCE'].std())

# mean of the difference of CRS departure and actual departure times
print((flights['CRS_DEP_TIME'] - flights['DEP_TIME']).mean())
