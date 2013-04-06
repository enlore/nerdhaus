from flask import Flask, request, render_template
from bill import Bill

app = Flask(__name__)

app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'

app.debug = True

@app.route('/', methods = ['GET'])
def index():
    bills = []
    gw_bill = Bill()
    elec_bill = Bill()
    rent = Bill()

    bills.append(gw_bill)
    bills.append(elec_bill)
    bills.append(rent)

    return render_template('index.html', bills = bills)




if __name__ == '__main__':
    app.run()
