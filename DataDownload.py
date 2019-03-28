# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:28:45 2019

@author: andy.lv
"""

class DataDownLoad(a):
    
    def __init__(self,x=1):
        pass
    
    def downloadData():
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
        ylbl_url='http://quotes.money.163.com/f10/zycwzb_{code}.html?type=year'
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
