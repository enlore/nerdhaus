from flask import Flask, request, render_template, g, redirect, url_for, flash
import sqlite3
from bill import Bill

app = Flask(__name__)

app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'

app.debug = True

app.database = 'db/nerdhaus.db'

def breakpoint():
    assert app.debug == False

def connect_db():
    return sqlite3.connect(app.database)

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

    bills = [dict(name=row[0], due_amount=row[1], late_amount=row[2], 
        due_date=row[3], late_after_date=row[4], termination_date=row[5], 
        pay_to=row[6]) for row in cur.fetchall()]

    return render_template('index.html', bills = bills)

@app.route('/new', methods = ['GET'])
def new_bill():
    return render_template('new_bill.html')

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
            request.form['termination_date']
        ])

    g.db.commit()

    return redirect(url_for('index'))

@app.route('/delete/<bill_name>', methods = ['DEL'])
def delete(bill_name):
    g.db.execute('DEL from bills where name=?', bill_name)
    g.db.commit()

    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()
