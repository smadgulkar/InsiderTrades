from flask import render_template, url_for,request,jsonify
from myapp2 import app,db
from myapp2.models import Filings,FilingsSchema,quotes,quotesSchema
import datetime
from sqlalchemy import or_

@app.route('/',methods=['GET','POST'])
@app.route('/index')
def index():
	page = request.args.get('page', 1, type=int)
	test = Filings.query.filter(Filings.TransactionType =='Acquisition',or_(Filings.ModeofAcquisition =='Market',Filings.ModeofAcquisition =='Market Purchase')).order_by(Filings.ReportedtoExchange.desc()).paginate(page,app.config['POSTS_PER_PAGE'],False)#
	if request.method == 'POST':
		name = request.form.get('search')
		test = Filings.query.filter(Filings.SecurityName.contains(name)).order_by(Filings.ReportedtoExchange.desc()).paginate(page,app.config['POSTS_PER_PAGE'],False)
	return render_template('home.html',test=test)#,next_url=next_url, prev_url=prev_url)

@app.route('/about')
def blogs():
	return render_template('about.html')

@app.route('/display')
def display():
	return render_template('display.html')

@app.route('/quotes/<int:code>',methods=['GET','POST'])
def getQuote(code):
	quote = quotes.query.with_entities(quotes.Date,quotes.Close).filter_by(SecurityCode=code).all()
	output = quotesSchema(many=True,strict=True).dump(quote).data
	return jsonify(output)

@app.route('/transactions/<int:code>',methods=['GET','POST'])
def getFiling(code):
	trades = Filings.query.with_entities(Filings.ReportedtoExchange,Filings.NameofPerson).filter(Filings.SecurityCode==code,Filings.TransactionType =='Acquisition',or_(Filings.ModeofAcquisition =='Market',Filings.ModeofAcquisition =='Market Purchase')).order_by(Filings.ReportedtoExchange.desc()).all()
	output = FilingsSchema(many=True,strict=True).dump(trades).data
	return jsonify(output)