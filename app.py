from flask import Flask, request, render_template

app = Flask(__name__)

app.secret_key = 'a;lskfdjaio;enfas;lknev;soi8evnse'

app.debug = True

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
