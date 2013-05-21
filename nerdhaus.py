from flask import Flask, request, render_template, g, redirect, url_for, flash
import bill
from contextlib import closing
import datetime
from sqlalchemy import create_engine
import db

app = Flask(__name__)
app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'
app.debug = True
app.database = 'db/nerdhaus.db'


@app.route('/', methods = ['GET'])
def index():
    return 'index page bro'

@app.route('/new', methods = ['GET'])
def new_bill():
    form = BillForm()
    return render_template('new_bill.html', form = form)

@app.route('/create_bill', methods = ['POST'])
def create_bill():
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
