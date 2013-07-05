from flask import render_template, abort
from nerdhaus import app

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except:
        abort(404)

