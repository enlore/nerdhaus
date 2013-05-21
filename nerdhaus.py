from flask import Flask, request, render_template, g, redirect, url_for, flash
from bill import Bill, BillForm
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import db

app = Flask(__name__)
app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'
app.debug = True

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

@app.route('/', methods = ['GET'])
def index():
    s = Session()
    bills = s.query(Bill).order_by(Bill.date_due)
    return render_template('index.html', bills = bills)

@app.route('/new', methods = ['GET'])
def new_bill():
    form = BillForm()
    return render_template('new_bill.html', form = form)

@app.route('/create_bill', methods = ['POST'])
def create_bill():
    form = request.form
    bill = Bill(
            form['name'],
            form['pay_to'],
            form['amount_due'],
            date(form['date_due'].split('/')),
            form['amount_late'],
            date(form['date_late'].split('/')),
            date(form['date_termination'].split('/'))
            )

    session = Session()
    session.add(bill)
    session.commit()

    return redirect(url_for('index'))

@app.route('/edit_bill/<int:bill_id>', methods = ['GET'])
def edit_bill(bill_id):
    return render_template('edit_bill.html', form = form)

@app.route('/update_bill', methods = ['POST'])
def update_bill():
    return 'update bill uri'

@app.route('/delete/<int:bill_id>', methods = ['GET'])
def delete(bill_id):
    return 'delete bill uri'

if __name__ == '__main__':
    app.run()
