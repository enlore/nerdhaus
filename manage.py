from flask.ext.script import Manager, Server
from nerdhaus import create_app
from nerdhaus.extensions import db

manager = Manager(create_app)

@manager.command
def init_db():
    """Initialize yon database"""
    db.drop_all()
    db.create_all() 

manager.add_command('run', Server(port=9005, host='127.0.0.1'))
manager.add_option('-c', '--config', dest='config', required=False)

if __name__ == '__main__':
    manager.run()
