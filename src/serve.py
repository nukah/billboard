from bottle import request, route, template, app, debug, run
from model import Database, Session, Events
from board import attain_feed
from time import mktime, strptime
from datetime import datetime

class DatabaseMiddleware(object):
    def __init__(self, app):
        global session
        session = Session()
        self.app = app
        self.db = Database()
        self.db.destroy()
        self.db.init()
    def __call__(self, env, start):
        return self.app(env, start)

def get_element_by_id(index):
    fields = ['date', 'title', 'descr', 'status', 'link']
    return [field+str(index) for field in fields]

app = DatabaseMiddleware(app())
debug(True)

@route('/')
def index_page():
   return template('index')

@route('/check', method='POST')
def send_form():
    url = request.forms.get('url')
    if url:
        resultset = attain_feed(url)
    return template('results', r = resultset)

@route('/edit', method='POST')
def edit_form():
    e_count = request.forms.get('amount')
    for index in xrange(int(e_count)):
        keys = get_element_by_id(index)
        element = dict([(key.rstrip(str(index)),request.forms.get(key)) for key in keys])
        if element['status'] == 'on':
            try:
                date = datetime.fromtimestamp(mktime(strptime(element['date'], '%d/%m/%Y %H:%M')))
            except ValueError, e:
                return 'Error in time data'
            new = Events(element['title'], \
                         element['link'], \
                         date, \
                         element['descr'])
            session.add(new)
    session.commit()
    return template('edit', r = request.forms)

run(reloader=True)
