from flask import Blueprint, render_template, abort

frontend = Blueprint('frontend', __name__)

@frontend.route('/', methods = ['GET'])
def index():
    return render_template('frontend/index.html')

@frontend.route('/blog/', methods=['GET'])
def blog_index():
    return render_template('blog/index.html')

@frontend.route('/blag/', methods=['GET'])
def blag_index():
    return render_template('blag/index.html')

@frontend.route('/shows/', methods=['GET'])
def shows_index():
    return render_template('shows/index.html')

@frontend.route('/portfolio/', methods=['GET','POST'])
def portfolio_index():
    return render_template('portfolio.html')

@frontend.route('/pages/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except:
        abort(404)

