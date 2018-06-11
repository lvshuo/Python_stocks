# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:13:34 2018

@author: andy.lv
"""
from time import sleep
from datetime import datetime
from pandas.core.frame import DataFrame
import urllib.request as w
import pandas as pd
import tushare as c
import os,stat
import matplotlib.pyplot as plt
import numpy as np
import platform 
import sys

##------------------------初始化变量---------------------------------------
x_data1=[2017,2016,2015,2014,2013,2012]
x_data2=[2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005]
x_data=[]
y_init_data_10year=[0,0,0,0,0,0,0,0,0,0]
y_init_data_5year=[0,0,0,0,0]
y_init_data_3year=[0,0,0]
y_init_data=[]
y_liability_short_interest=[]
y_liability_long_interest=[]
y_ponds_interest=[]
label_dict={'Rev':'Revenue','Cash':'Cash Flow'}
url_mac='/Users/shuolv/Python/code-finace/data/'
url_window='data/'
m_this_year=2017 ##


ROE_row='净资产收益率(%)'
Acountable_money='应收账款周转天数(天)'
Total_asset_turnover='总资产周转率(次)'
Net_profit_gross='净利润增长率(%)'
Total_Liability='资产负债率(%)'

##----------------获取操作系统--------
def UsePlatform():
    User_systerm=platform.system()
    return User_systerm


#####----------------------操作系统判断--------------------------------
user_platform=UsePlatform()

if user_platform =='Windows' or  user_platform =='Win32':
    url_comman=url_window
else:
    url_comman=url_mac

print(url_comman)

##--------------------字符串转换----------------------
def _tcode(s):
    l = len(str(s))
    v = str(s)
    if(l>6):
        return v[:6]
    elif l==6:
        return v
    else:
        return ('0'*(6-l))+v
##---------------------基础数据下载------------------------------------
def _download(url,to_file):
    i_error=0
    i_new=0
    i_update=0
    if not os.path.exists(to_file): # 判读文件是否存在，若不存在则下载文件
    
        try:
                  
            w.urlretrieve(url.format(code=_tcode(codes)),to_file)
            i_new=i_new+1
            sleep(3)
        except Exception as e:
        
            i_error = i_error + 1
        else: # 若文件过时，则更新文件
    
            if (datetime.now()-datetime.fromtimestamp(os.stat(to_file)[stat.ST_CTIME])).days>=90:
        
                try:
                    w.urlretrieve(url.format(code=_tcode(codes)),to_file)
                    i_update=i_update+1
                    sleep(3)
                except Exception as e:
            
                    i_error=i_error+1   
##--------------------------数据转换-------------------

def _csv_data2int_data(file_cvs,start_index,y_data):
    
    if user_platform== 'Windows':  
        f_csv_read=open(file_cvs)
        f_csv=pd.read_csv(f_csv_read)  # For windows
        f_csv_read.close()
        
    else:
        f_csv=pd.read_csv(file_cvs,encoding='gb2312')  #For Mac os
  
    f_csv2np=np.array(f_csv.iloc[start_index,:])
    
#    f_csv=pd.read_excel(file_cvs)
#    f_csv=DataFrame(f_csv)
#    f_csv2np=f_csv.iat[start_index,:]

    
    temp=len(f_csv2np)-3
    if(temp>=10):
        y_data_plot=[0,0,0,0,0,0,0,0,0,0]
    elif(temp>=5 and temp<10):
        y_data_plot=[0,0,0,0,0]
    elif(temp>=3 and temp<5):
        y_data_plot=[0,0,0]
        

#    
    
#    for i in range(len(f_csv2np)-3):
#        y_data.append([0])
#       
#        print(y_data[i])
    #y_data_temp=np.array(y_data)
    #y_data=np.array(y_data)
    #y_data_plot=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(y_data_plot)):
        if f_csv2np[i+1]=='--':
            f_csv2np[i+1]='0'
        #y_data.append(y[i+1])
        #print(f_csv2np[len(f_csv2np)-2])
        #print(f_csv2np[len(f_csv2np)-1])
        y_data_plot[i]=float(f_csv2np[i+1])
        #print(y_data[i])
    return y_data_plot
##----------------------X_data转换--------------------------
def _get_x_data(y_data):## 根据y_data 确定x_data
    for i in range(len(y_data)):
        x_data.append([m_this_year-i]) ##2017年
        #print(x_data[i])
        
    return x_data

    

 ##-----------------绘图------------------------------------------     
              
def _matlibplot(f2plot,x_data1,y_data1,start_index,y_label):
    df=pd.read_excel(f2plot)
    df=DataFrame(df)
    data_range=df.columns.size-1
    #print(data_range)
    for s in range(data_range):
        y_data1.append(df.iat[start_index,s+1]) 
        
    y_data1=np.array(y_data1)   
    x_data1=np.array(x_data1)
    if y_label=='Revenue':
        for i in range(len(y_data1)):
            y_data1[i]=round(int(y_data1[i])/10000,2)
        plt.plot(x_data1,y_data1,'bo--',linewidth=2)
        plt.grid(True)
        plt.ylabel(y_label)
        plt.show()
    else:
       
        plt.plot(x_data1,y_data1,'bo--',linewidth=2)
        plt.grid(True)
        plt.ylabel(y_label)
        plt.show()
####-------------excel 文件转换为int-------------------------
def _excel2int(filet2int,data_range,y_data):
    df=pd.read_excel(f_zycw)
    df=DataFrame(df)
    for s in range(data_range):
        y_data[s]=float(df.iat[start_index,s+1])
    return y_data
        
#######------------------------CSV转化为Excel文件---------------
def _csv2excel(csvfile,excelfile):
    f=open(csvfile,encoding='gb2312')
    csv=pd.read_csv(f)
    csv.to_excel(excelfile,sheet_name='data')
    f.close()
###------------------------------------------------------------
code_num = input ('请输入代码')
codes=int(code_num)
#names=str(codes)
#############---------------判断对应的公司名称-----------------

if not os.path.exists(url_comman):
    os.mkdir(url_comman)
else:
    pass
    
c_sbf=url_comman+'stocks_b.csv'

if not os.path.exists(c_sbf):
    c.get_stock_basics().to_csv(c_sbf) #下载现在的股票代码
else: # 若文件过时，则更新文件
    if (datetime.now()-datetime.fromtimestamp(os.stat(c_sbf)[stat.ST_CTIME])).days>=90:
       c.get_stock_basics().to_csv(c_sbf)
        
   
stocks_b = pd.read_csv(url_comman+'stocks_b.csv') 

codes_b = stocks_b['code']
names_b = stocks_b['name']

for v in range(len(codes_b)):
    if codes ==codes_b[v]:
        names=names_b[v]
        
print(codes)

print(names)

path2save=url_comman+names+'/'
if not os.path.exists(path2save):
    os.mkdir(path2save)
else:
    pass
####------------------------判断数据所在行数-----------------------
def _get_csv_data_row(f_excel,accounts):
    df=pd.read_excel(f_excel)
    df=DataFrame(df)
    csv_rows=df.iloc[:,0].size 
    
    #print(csv_rows)
    for s in range(csv_rows):
        if df.iat[s,0]==accounts:
            row_return =s
            break
        else:
            row_return=0
    #print(row_return)  
    return row_return
       
       # y_data1.append(df.iat[start_index,s+1]) 
    
   ## '净资产收益率(%)'

#############---------------下载资产负债表-----------------
bs_url = 'http://quotes.money.163.com/service/zcfzb_{code}.html?type=year'
#to_file_template = 'data/bs{code}.csv'
to_file_template=path2save+'资产负债表-'+names+'.csv'
to_file = to_file_template.format(code=_tcode(codes))
print(str(datetime.now()),'正在下载',names,'资产负债表')
_download(bs_url,to_file)

to_file_xlsx=path2save+'资产负债表-'+names+'.xlsx'

_csv2excel(to_file_template,to_file_xlsx)

#os.remove(to_file_template)

#########-----------------下载利润表---------------------------------------
             
is_url = 'http://quotes.money.163.com/service/lrb_{code}.html?type=year'
#to_file_template = 'data/is{code}.csv'
to_file_template=path2save+'利润表-'+names+'.csv'

to_file = to_file_template.format(code=_tcode(codes))
print(str(datetime.now()),'正在下载',names,'利润表')
_download(is_url,to_file)

to_file_xlsx=path2save+'利润表-'+names+'.xlsx'
_csv2excel(to_file_template,to_file_xlsx)
#os.remove(to_file_template)


########------------------------下载现金流量表------------------------------
cf_url = 'http://quotes.money.163.com/service/xjllb_{code}.html?type=year'
#to_file_template = 'data/cf{code}.csv'
to_file_template=path2save+'现金流量表-'+names+'.csv'
to_file = to_file_template.format(code=_tcode(codes))
print(str(datetime.now()),'正在下载',names,'现金流量表')
_download(cf_url,to_file)   
to_file_xlsx=path2save+'现金流量表-'+names+'.xlsx'
_csv2excel(to_file_template,to_file_xlsx)      
#os.remove(to_file_template)

######----------------------其他财务比率--------------------------
ylbl_url='http://quotes.money.163.com/f10/zycwzb_{code},year.html'
#to_file_template = 'data/ylbl{code}.xlsx'
#to_file=to_file_template.format(code=_tcode(codes))

print(str(datetime.now()),'正在下载',names,'主要财务比率')

tables = pd.read_html(ylbl_url.format(code=_tcode(codes)))

Path_table5=path2save+'主要财务指标-' + names+ '.xlsx'
Path_table6=path2save+'盈利能力-' + names + '.xlsx'
Path_table7=path2save+'成长能力-' + names + '.xlsx'
Path_table8=path2save+'偿还能力-' + names + '.xlsx'

i=0
for table in tables:
    
    if i>=5:       
        if i==5:
            if os.path.exists(Path_table5):
                pass
            else:
                DataFrame(table).to_excel(Path_table5)
        if i==6:
            if os.path.exists(Path_table6):
                pass
            else:
                DataFrame(table).to_excel(Path_table6)
            
        if i==7:
            if os.path.exists(Path_table7):
                pass
            else:
                DataFrame(table).to_excel(Path_table7)
             
        if i==8:
            if os.path.exists(Path_table8):
                pass
            else:
                DataFrame(table).to_excel(Path_table8)
        i += 1        
    else:
        i+=1

###初始化
#######--------------------------近五年财务指标绘图----------------------------

##--------------------ROE--------------------------

print('---------------------------ROE-----------------------')
#start_index=7 #ROE 数据行数
y_data1=[]
#data_range=6
f_zycw=path2save+'主要财务指标-' + names+ '.xlsx'
start_index=_get_csv_data_row(f_zycw,ROE_row)
y_label='ROE %'
_matlibplot(f_zycw,x_data1,y_data1,start_index,y_label)

##------------------应收账款周转天数--------------------------------------------
print('------------------应收账款周转天数-----------------------')
f_zycw=path2save+'偿还能力-' + names+ '.xlsx'
start_index=_get_csv_data_row(f_zycw,Acountable_money) #应收账款周转天数所在行数 
y_data1=[]
data_range=6
y_label='Accounts receivable turnover days'
_matlibplot(f_zycw,x_data1,y_data1,start_index,y_label)
##------------------总资产周转率--------------------------------------------
print('------------------总资产周转率-----------------------')
f_zycw=path2save+'偿还能力-' + names+ '.xlsx'
start_index=_get_csv_data_row(f_zycw,Total_asset_turnover) #应收账款周转天数所在行数 
y_data1=[]
data_range=6 
y_label='Total Assets Turnover %'
_matlibplot(f_zycw,x_data1,y_data1,start_index,y_label)
##------------------净利润增长率--------------------------------------------
print('------------------净利润增长率-----------------------')
f_zycw=path2save+'成长能力-' + names+ '.xlsx'
start_index=_get_csv_data_row(f_zycw,Net_profit_gross) #应收账款周转天数所在行数 
y_data1=[]
data_range=6 
y_label='Net profit growth rate %'
_matlibplot(f_zycw,x_data1,y_data1,start_index,y_label)
##------------------资产负债率--------------------------------------------
print('------------------资产负债率-----------------------')
f_zycw=path2save+'盈利能力-' + names+ '.xlsx'
start_index=_get_csv_data_row(f_zycw,Total_Liability) #应收账款周转天数所在行数 
y_data1=[]
data_range=6 
y_label='Assets and liabilities %'
_matlibplot(f_zycw,x_data1,y_data1,start_index,y_label)
##------------------近年营收--------------------------------------------
print('------------------近年营收（万）-----------------------')
f_revenue=path2save+'利润表-' + names+ '.csv'
start_index=0 #营业收入所在行数 
y_revenue_data=y_init_data_10year
x_data=[]
data_range=13
y_label='Revenue'

y_revenue_data=_csv_data2int_data(f_revenue,start_index,y_revenue_data)


x_data=_get_x_data(y_revenue_data)
 
plt.plot(np.array(x_data),y_revenue_data,'bo--',linewidth=2)
plt.grid(True)
plt.ylabel(y_label)
plt.show()



##------------------近年营收--------------------------------------------
print('------------------应收账款（万）-----------------------')
f_account_receivable=path2save+'资产负债表-' + names+ '.csv'
start_index=6 #应收账款所在行数 
x_data=[]
y_account_receivable_data=y_init_data_10year
data_range=13
y_label='Account Receivable'
    
y_account_receivable_data=_csv_data2int_data(f_account_receivable,start_index,y_account_receivable_data)

x_data=_get_x_data(y_account_receivable_data)

plt.plot(x_data,y_account_receivable_data,'bo--',linewidth=2)
#plt.bar(np.array(x_data2),y_data)
plt.grid(True)
plt.ylabel(y_label)
plt.show()

###--------------------总负责比率与有息负债比率-----------------------------------
print('------------------负债率对比（%）-----------------------Liabilities')

x_data=[]

f_liability_short_interest=path2save+'资产负债表-' + names+ '.csv'

start_short_index=52 #短期借款所在行数 
y_liability_short_interest=y_init_data_10year
y_liability_short_interest_plot=_csv_data2int_data(f_liability_short_interest,start_short_index,y_liability_short_interest)

#y_liability_short_interest_plot=y_liability_short_interest
#print('short',y_liability_short_interest_plot)

f_liability_long_interest=path2save+'资产负债表-' + names+ '.csv'
start_long_index=84 #长期借款所在行数
y_liability_long_interest=[]
y_liability_long_interest=_csv_data2int_data(f_liability_long_interest,start_long_index,y_liability_long_interest)

#print('long',y_liability_long_interest)

f_ponds_interest=path2save+'资产负债表-' + names+ '.csv'
start_ponds_index=85#应付债券所在行数
y_ponds_interest=y_init_data_10year
y_ponds_interest=_csv_data2int_data(f_ponds_interest,start_ponds_index,y_ponds_interest)
#print('ponds',y_ponds_interest)



##有息负债总数
y_total_liability_interest=np.array(y_liability_short_interest_plot)+np.array(y_liability_long_interest)+np.array(y_ponds_interest)
#y_total_liability_interest
#print('total interest',y_total_liability_interest)

##总负责
f_total_liability=path2save+'资产负债表-' + names+ '.csv'
start_total_liability_index=93
y_total_liability=y_init_data_10year
y_total_liability=_csv_data2int_data(f_total_liability,start_total_liability_index,y_total_liability)
#print('total liability',y_total_liability)
##资产总数
f_total_asset=path2save+'资产负债表-' + names+ '.csv'
start_asset_index=51
y_total_asset=y_init_data_10year
y_total_asset=_csv_data2int_data(f_total_asset,start_asset_index,y_total_asset)
#print('total asset',y_total_asset)


y_liability_interest_per=np.array(y_total_liability_interest)/np.array(y_total_asset)

y_total_liability_per=np.array(y_total_liability)/np.array(y_total_asset)


x_data=_get_x_data(y_ponds_interest) ##获取X坐标

y_label='Liability %'
    
plt.plot(x_data,y_liability_interest_per*100,'bo--',linewidth=2,label='Liability interest')
plt.plot(x_data,y_total_liability_per*100,'ro--',linewidth=2,label='Total Liability')
plt.legend(loc='upper left')
#plt.bar(np.array(x_data2),y_data)
plt.grid(True)
plt.ylabel(y_label)
plt.show()

##------------------近年净利润--------------------------------------------
print('------------------近年净利润-----------------------')
f_net_profit=path2save+'利润表-' + names+ '.csv'
start_index=40 #净利润所在行数 
y_net_profit_data=[0,0,0,0,0,0,0,0,0,0] ##y_init_data_10year
data_range=13
x_data=[]
y_label='Net profit'

y_net_profit_data=_csv_data2int_data(f_net_profit,start_index,y_net_profit_data)

x_data=_get_x_data(y_net_profit_data) ##获取X坐标
#y_data=np.array(y_data)
plt.plot(x_data,y_net_profit_data,'bo--',linewidth=2)
plt.grid(True)
plt.ylabel(y_label)
plt.show()
##------------------现金流量净额--------------------------------------------
print('------------------现金流量净额-----------------------')
f_net_cashflow=path2save+'现金流量表-' + names+ '.csv'
start_index=24 #现金流量净额所在行数 
y_net_cashflow_data=y_init_data_10year
data_range=13
x_data=[]
y_label='Net Cash Flow (10 th)'

y_net_cashflow_data=_csv_data2int_data(f_net_cashflow,start_index,y_net_cashflow_data)


x_data=_get_x_data(y_net_cashflow_data) ##获取X坐标  
#y_data=np.array(y_data)
plt.plot(x_data,y_net_cashflow_data,'bo--',linewidth=2,label='Net Cash')
plt.grid(True)
plt.ylabel(y_label)
plt.show()
###-------------------数据对比-------------------

print('---------------------数据对比---------------------')


plt.plot(x_data,y_revenue_data,'bo--',linewidth=2,label='Revenue')
plt.plot(x_data,y_net_profit_data,'go--',linewidth=2,linestyle='--',label='Net profit')
plt.plot(x_data,y_account_receivable_data,'ro--',linewidth=2,label='Accounts Receivable')
plt.plot(x_data,y_net_cashflow_data,'yo--',linewidth=2,label='Net Cash')
plt.grid(True)
plt.legend(loc='upper left')
plt.ylabel(y_label)
plt.show()



