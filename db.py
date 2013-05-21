import sqlite3

def connect_db():
    return sqlite3.connect(app.database)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema/schema.sql') as schema:
            db.cursor().executescript(schema.read())
        db.commit()
