from flask import render_template, abort
from nerdhaus import app

@app.route('/', methods = ['GET'])
def index():
    return render_template('frontend/index.html')

@app.route('/blog/', methods=['GET'])
def blog_index():
    return render_template('blog/index.html')

@app.route('/portfolio/', methods=['GET','POST'])
def portfolio_index():
    return render_template('portfolio.html')

@app.route('/pages/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except:
        abort(404)

