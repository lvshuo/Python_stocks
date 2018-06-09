# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:26:48 2018

@author: andy.lv
"""
import tushare as c
import os 
import pandas as Pd

c_sbf = 'data/stocks_b.csv' 

#if not os.path.exists(c_sbf):
 #   c.get_stock_basics().to_csv(c_sbf)

stocks_b = Pd.read_csv('data/stocks_b.csv') 


codes = stocks_b['code']

names = stocks_b['name']

print(codes)

print(names)

print(type(codes[2]))



