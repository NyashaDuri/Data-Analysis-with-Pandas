#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# load the flights dataset
flights = pd.read_csv('flights.csv', index_col=False)

# plot a histogram of CRS departure times
flights['CRS_DEP_TIME'].hist()

# plot a histogram of CRS arrival times
flights['CRS_ARR_TIME'].hist()

# plot average distance that flights travel by month
flights_by_month = flights.groupby('MONTH')
flights_by_month['DISTANCE'].aggregate(np.mean).plot()

# plot average distance that flights travel by day of the week
flights_by_day_of_week = flights.groupby('DAY_OF_WEEK')
flights_by_day_of_week['DISTANCE'].aggregate(np.mean).plot()
