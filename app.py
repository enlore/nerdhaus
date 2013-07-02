from flask import Flask, request, render_template, abort
import random

app = Flask(__name__)

app.secret_key = 'a;lskfdjaio;enfas;lknev;soi8evnse'

app.debug = True

@app.errorhandler(404)
def not_found(error):
    gifs = [
    'gangnamvator.gif',
    'hammer_duo.gif',
    'Hammertime.gif',
    'mc_hammer.gif',
    'Mc Hammer Zidane Trick-329529.gif',
    'Only_6c1fbe_419666.jpg',
    'pancake_dj.gif',
    ]

    gif = random.choice(gifs)
    return render_template('404.html', gif=gif)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except:
        abort(404)

if __name__ == '__main__':
    app.run()
