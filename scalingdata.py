# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:11:01 2021

@author: Jamie Stephens
"""
import pandas as pd
import numpy as np
from scipy.io import arff
from numpy import genfromtxt
from pymfe.mfe import MFE
import csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import eda



df = eda.df
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)

print(df.apply(lambda x: pd.Series([x.min(), x.max()])).T.values.tolist())

print(scaled)
print(scaled.apply(lambda x: pd.Series([x.min(), x.max()])).T.values.tolist())