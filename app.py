from flask import Flask, request

app = Flask(__name__)

app.secret_key = 'a;lskfdjaio;en lol dev key fas;lknev;soi8evnse'

app.debug = True

@app.route('/', methods = ['GET'])
def index():
    return 'hey'



if __name__ == '__main__':
    app.run()
