import pandas as pd 
import sqlite3
import datetime 
import datetime
from sqlalchemy import create_engine

conn = sqlite3.connect('/home/shubhankar/.virtualenvs/trader/heroku/bseData.db')
df = pd.read_sql('SELECT SecurityCode FROM tbCoMapping',conn)
k = df['SecurityCode'].tolist()

for i in k:
	url = 'https://api.bseindia.com/BseIndiaAPI/api/DwnldExcelIT15/w?scripcode={0}&fromdt=&todt=&flag=InsiderTrade15'
	try:
		df2 = pd.read_csv(url.format(i),parse_dates=['Reported to Exchange'])
	except Exception as e:
		print('Error getting data for {0}, moving on..'.format(i))
		continue
	print('Gathering data for {0}'.format(i))
	ma_list =	[
		'SecurityCode',
		'SecurityName',
		'NameofPerson',
		'Categoryofperson',
		'TypeofSecuritiesBefore', 
		'NumShareholdingBefore',
		'PctShareholdingBefore', 
		'TypeofSecuritiesTransacted', 
		'NumberofSecuritiesTransacted', 
		'ValueofSecuritiesTransacted', 
		'TransactionType', 
		'TypeofSecuritiesAfter',
		'NumShareholdingAfter', 
		'PctShareholdingAfter', 
		'TransactionDateFrom', 
		'TransactionDateTo', 
		'DateofIntimationtoCompany', 
		'ModeofAcquisition', 
		'DerivativeType', 
		'DerivativeContractSpec', 
		'DerivativesBuyValue', 
		'DerivativesBuyUnits', 
		'DerivativesSaleValue',
		'DerivativesSaleUnits', 
		'Exchange', 
		'ReportedtoExchange'
	]
	engine = create_engine('sqlite:////home/shubhankar/.virtualenvs/trader/local/myapp2/site.db')
	df2.columns= ma_list
	df3 = pd.read_sql('SELECT * FROM Filings where SecurityCode = (?)',engine,params=(i,))
	df4 = df2[~df2.ReportedtoExchange.isin(df3.ReportedtoExchange.values)]
	df4.to_sql('Filings',con=engine,if_exists='append',index=False)
conn.close()