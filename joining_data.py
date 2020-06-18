#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

# load the flights dataset
flights = pd.read_csv('flights.csv', index_col=False)

# load the mapping CSV file
days_of_week = pd.read_csv('L_WEEKDAYS.csv', index_col=False)

# combine two dataframes on flights['DAY_OF_WEEK'] and days_of_week['CODE']
merged = pd.merge(flights, days_of_week, left_on='DAY_OF_WEEK', right_on='Code')

# remove the DAY_OF_WEEK and Code columns (inplace=True)
merged.drop(columns=['DAY_OF_WEEK', 'Code'], inplace=True)
# rename Description -> DAY_OF_WEEK
merged.rename(columns={'Description': 'DAY_OF_WEEK'}, inplace=True)
