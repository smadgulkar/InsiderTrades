import pandas as pd 
import sqlite3
import datetime 
import datetime
from myapp2 import db

conn = sqlite3.connect('/home/shubhankar/.virtualenvs/trader/heroku/bseData.db')
df = pd.read_sql('SELECT SecurityCode FROM tbCoMapping',conn)
k = df['SecurityCode'].drop_duplicates().tolist()

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
	conn2 = sqlite3.connect('/home/shubhankar/.virtualenvs/trader/local/myapp2/site.db')
	df2.columns= ma_list
	# df2.to_sql('Filings',con=conn2,if_exists='append')
	db.session.add(df2)
	print('Completed data for {0}'.format(i))
db.session.commit()