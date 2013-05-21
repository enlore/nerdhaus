from flask import Flask, request, render_template, g, redirect, url_for, flash
from bill import Base, Bill, BillForm
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'
app.debug = True

engine = create_engine('sqlite:///db/nerdhaus.db', echo=True)
Session = sessionmaker(bind=engine)

def create_table():
    Base.metadata.create_all(engine)

def string_to_date(datestring):
    if '/' in datestring:
        sep = '/'
    elif '-' in datestring:
        sep = '-'
    y, m, d = datestring.split(sep)
    return date(int(y), int(m), int(d))

def dollars_to_cents(amount):
    d = float(amount)
    return d * 100

if app.debug:
    create_table()

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
            dollars_to_cents(form['amount_due']),
            string_to_date(form['date_due']),
            dollars_to_cents(form['amount_late']),
            string_to_date(form['date_late']),
            string_to_date(form['date_termination']),
            )

    session = Session()
    session.add(bill)
    session.commit()

    return redirect(url_for('index'))

@app.route('/edit_bill/<int:bill_id>', methods = ['GET'])
def edit_bill(bill_id):
    s = Session()
    bill = s.query(Bill).filter_by(id=bill_id).first()
    form = BillForm(obj=Bill)
    return render_template('edit_bill.html', form = form)

@app.route('/update_bill', methods = ['POST'])
def update_bill():
    return 'update bill uri'

@app.route('/delete/<int:bill_id>', methods = ['GET'])
def delete(bill_id):
    s = Session()
    bill = s.query(Bill).filter_by(id=bill_id).first()
    s.delete(bill)
    s.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
