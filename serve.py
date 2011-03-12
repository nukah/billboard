import bottle
from model import Database, Session, Events

class DatabaseMiddleware(object):
    def __init__(self, app):
        global session
        session = Session()
        self.app = app
        self.db = Database()
    def __call__(self, env, start):
        self.db.init()
        return self.app(env, start)
    
app = DatabaseMiddleware(bottle.app())

@bottle.route('/')
def index_page():
    objects = session.query(Events).all()
    return objects

bottle.run(app=app)