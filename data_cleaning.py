#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# loads our flights dataset
flights = pd.read_csv('flights.csv', index_col=False)

# converting columns to their appropriate data types
flights['FL_DATE'] = pd.to_datetime(flights['FL_DATE'])
flights['CANCELLED'] = flights['CANCELLED'].astype(np.bool)
flights['DIVERTED'] = flights['DIVERTED'].astype(np.bool)

# remove columns YEAR, MONTH, DAY_OF_MONTH
flights.drop(columns=['YEAR', 'MONTH', 'DAY_OF_MONTH'], inplace=True)

# rename columns
flights.rename(columns={'DEST': 'DESTINATION'}, inplace=True)

# get number of null values per column
print(flights.isnull().sum())

# difference in CRS departure time and actual departure time
print(flights['CRS_DEP_TIME'] - flights['DEP_TIME'])

# drop NaN/null/missing values
print((flights['CRS_DEP_TIME'] - flights['DEP_TIME']).dropna())
