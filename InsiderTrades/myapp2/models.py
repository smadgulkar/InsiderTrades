from datetime import datetime
from myapp2 import db,ma

class Filings(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	SecurityCode = db.Column(db.Integer)
	SecurityName = db.Column(db.String(120))
	NameofPerson = db.Column(db.String(120))
	Categoryofperson = db.Column(db.String(120))
	TypeofSecuritiesBefore = db.Column(db.String(120))
	NumShareholdingBefore = db.Column(db.String(120))
	PctShareholdingBefore = db.Column(db.Float(50))
	TypeofSecuritiesTransacted = db.Column(db.String(120))
	NumberofSecuritiesTransacted = db.Column(db.Integer)
	ValueofSecuritiesTransacted = db.Column(db.String(120))
	TransactionType =db.Column(db.String(120))
	TypeofSecuritiesAfter = db.Column(db.String(120))
	NumShareholdingAfter = db.Column(db.Integer)
	PctShareholdingAfter = db.Column(db.Integer)
	TransactionDateFrom = db.Column(db.String)
	TransactionDateTo = db.Column(db.String)
	DateofIntimationtoCompany = db.Column(db.String)
	ModeofAcquisition  = db.Column(db.String(120))
	DerivativeType  = db.Column(db.String(120))
	DerivativeContractSpec  = db.Column(db.String(120))
	DerivativesBuyValue  = db.Column(db.String(120))
	DerivativesBuyUnits  = db.Column(db.String(120))
	DerivativesSaleValue = db.Column(db.String(120))
	DerivativesSaleUnits  = db.Column(db.String(120))
	Exchange  = db.Column(db.String(120))
	ReportedtoExchange=db.Column(db.Date)

class FilingsSchema(ma.ModelSchema):
	class Meta:
		model = Filings

class quotes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Date = db.Column(db.Date)
	Symbol = db.Column(db.String(120))
	Series = db.Column(db.String(120))
	PrevClose = db.Column(db.Float(50))
	Open = db.Column(db.Float(50))
	High = db.Column(db.Float(50))
	Low = db.Column(db.Float(50))
	Last = db.Column(db.Float(50))
	Close = db.Column(db.Float(50))
	VWAP = db.Column(db.Float(50))
	Volume = db.Column(db.Integer)
	Turnover = db.Column(db.Float(50))
	Trades = db.Column(db.Integer)
	DeliverableVolume = db.Column(db.Integer)
	SecurityCode = db.Column(db.Integer)

class quotesSchema(ma.ModelSchema):
	class Meta:
		model = quotes

class HiLo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Date = db.Column(db.Date)
	Symbol = db.Column(db.String(120))
	SecurityCode = db.Column(db.Integer)
	YearHigh = db.Column(db.Float(50))
	YearLow = db.Column(db.Float(50))
