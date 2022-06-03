'''
Created by Bryan R. Vallejo @BryanRVallejo
CCBY-0.3
Please do use this and share it with others :)
'''


from datetime import datetime
import pandas as pd

# read with Pandas
data = pd.read_csv(r'740.csv.gz', header=None, compression='gzip')

# change columns of OpenCell
col_names = ['radio', 'mcc', 'mnc', 'lac', 'cid', 'changeable_0',
            'long', 'lat', 'range', 'sample', 'changeable_1',
            'created', 'updated', 'avgsignal']

data.columns = col_names

#UMTS 3G, GSM 2G, LTE 4G, CDMA 3G

data['radio'] = data['radio'].replace('UMTS', '3G').replace('GSM', '2G').replace('LTE', '4G').replace('CDMA', '3G')

# 0 Movistar, 1 Claro, 2  CNT, 3 Tuenti

data = data.loc[data['mnc'].isin([0, 1, 3])]
data['mnc'] = data['mnc'].replace(0, 'Movistar').replace(1, 'Claro').replace(3, 'Tuenti')

data.to_csv(r'OpenCell_EC.csv')



#END
