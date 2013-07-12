from flask import Flask
from .frontend import frontend
from .blog import blog
import random

app = Flask(__name__)

app.secret_key = 'a;lskfdjaio;enfas;lknev;soi8evnse'

app.register_blueprint(frontend)
app.register_blueprint(blog)

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
    return render_template('errors/404.html', gif=gif)
