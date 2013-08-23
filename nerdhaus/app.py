from flask import Flask, render_template
from .frontend import frontend
from .blog import blog
from .extensions import login_manager
import random

BLUEPRINTS = [blog, frontend]

def create_app(app_name=__name__, config=None, blueprints=[]):
    app = Flask(app_name)
    configure_app(app, config)

    if not blueprints:
        blueprints = BLUEPRINTS

    bootstrap_blueprints(app, blueprints)
    register_extensions(app)
    return app

def bootstrap_blueprints(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp)

def configure_app(app, config):
    app.secret_key = 'a;lskfdjaio;enfas;lknev;soi8evnse'
    app.config.from_object(__name__)
    app.config.from_pyfile('settings.cfg')

def register_extensions(app):
    login_manager.init_app(app)

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


