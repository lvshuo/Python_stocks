# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:17:15 2018

@author: andy.lv
"""
import pandas as pd

code_num = input ('请输入代码')
codes=int(code_num)

stocks_b = pd.read_csv('data/stocks_b.csv') 

codes_b = stocks_b['code']
names_b = stocks_b['name']

for v in range(len(codes_b)):
    if codes ==codes_b[v]:
        names=names_b[v]

to_file_template='data/'+'资产负债表-'+names+'.csv'

to_file_xlsx='data/'+'资产负债表-'+names+'.xlsx'

f=open(to_file_template)

csv = pd.read_csv(f)
#csv=pd.read_csv(r'资产负债表-东方雨虹.csv',encoding='gb2312',header=None)

csv.to_excel(to_file_xlsx, sheet_name='data')

f.close()