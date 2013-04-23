from flask import Flask, request, render_template, g, redirect, url_for, flash
from wtforms import Form, TextField, DateField, DecimalField, validators
import sqlite3
from bill import Bill
from contextlib import closing
import datetime

app = Flask(__name__)
app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'
app.debug = True
app.database = 'db/nerdhaus.db'

def breakpoint():
    assert app.debug == False

def connect_db():
    return sqlite3.connect(app.database)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema/schema.sql') as schema:
            db.cursor().executescript(schema.read())
        db.commit()

class BillForm(Form):
    name = TextField(u'Name:', [validators.required()])
    pay_to = TextField(u'Pay To:',[validators.required()])
    due_date = DateField(u'Date Due:',[validators.required()])
    due_amount = DecimalField(u'Amount Due:',places = 2)
    late_after_date = DateField(u'Late After:',[validators.required()])
    late_amount = DecimalField(u'Late Amount:', places = 2)
    termination_date = DateField(u'Termination Date:',[validators.required()])


@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/', methods = ['GET'])
def index():
    cur = g.db.execute('SELECT * from bills')

    # needs to be objects
    bills = [dict(
            id=row[0],
            name = row[1],
            pay_to = row[2],
            due_amount = row[3],
            due_date = row[4],
            late_amount = row[5],
            late_after_date = row[6],
            termination_date = row[7]
        ) for row in cur.fetchall()
   ]

    if not bills: 
        flash('no bills')
        return render_template('index.html')

    bill_meta = {}

    today = datetime.date.today()
    smallest_delta = datetime.timedelta(9999)
    term_nearest = datetime.timedelta(9999)
    bill_name = None

    late_bills = []

    for bill in bills:
        # expects 'YYYY/MM/DD'
        date_tuple = bill['due_date'].split('/')

        bdate = datetime.date(
                    int(date_tuple[0]),
                    int(date_tuple[1]),
                    int(date_tuple[2])
                )
        tdelta = bdate - today

        if tdelta < smallest_delta and tdelta > datetime.timedelta(0):
            smallest_delta = tdelta
            bill_name = bill['name']

        if tdelta < datetime.timedelta(0):
            late_bills.append(bill['name'])

        y, m, d = bill['termination_date'].split('/')
        term_date = datetime.date(int(y), int(m), int(d))

        term_delta = term_date - today

        if term_delta < term_nearest:
            term_nearest = term_delta
            bill_meta['next_term'] = bill['name']
            
        
    bill_meta['next_due'] = today + smallest_delta
    bill_meta['next_due_name'] = bill_name
    bill_meta['late_list'] = late_bills
        
    for bill in bills:
        bill['split'] = bill['due_amount'] / 4

    return render_template(
            'index.html', 
            bills = bills, 
            bill_meta = bill_meta
            )

@app.route('/new', methods = ['GET'])
def new_bill():
    form = BillForm()
    return render_template('new_bill.html', form = form)

@app.route('/create_bill', methods = ['POST'])
def create_bill():
    sql = "INSERT INTO bills (name, pay_to, due_date, due_amount, late_amount," \
            + "late_after_date, termination_date) VALUES (?, ?, ?, ?, ?, ?, ?)"
    
    g.db.execute(sql, [
            request.form['name'],
            request.form['pay_to'],
            request.form['due_date'],
            request.form['due_amount'],
            request.form['late_amount'],
            request.form['late_after_date'],
            request.form['termination_date'],
        ])

    g.db.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:bill_id>', methods = ['GET'])
def delete(bill_id):
    g.db.execute('DELETE from bills where id=?', (bill_id,))
    g.db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
