from flask import Flask
from .frontend import frontend
from .blog import blog

app = Flask(__name__)
app.register_blueprint(frontend)
app.register_blueprint(blog)
