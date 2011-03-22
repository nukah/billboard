from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text

engine = create_engine('sqlite:///billboard.db', echo=True)
Base = declarative_base(bind=engine)

class Database(object):
    def init(self):
        Base.metadata.create_all()
    def destroy(self):
        Base.metadata.drop_all()

def Session():
    s = scoped_session(sessionmaker(bind = engine))
    return s()


## MODEL DECLARATION


class Events(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key = True)
    title = Column(String)
    link = Column(String)
    date = Column(DateTime)
    time = Column(DateTime)
    desc = Column(Text)
    
    def __init__(self, title = None, link = None, date = None, time = None, text = None):
        self.title = title.decode('utf-8')
        self.link = link
        self.date = date
        self.time = time
        self.desc = text.decode('utf-8') or ''
        
    def __repr__(self):
        return "<Event('%s','%s','%s','%s','%s')>" % (self.id, self.title, self.link, self.date, self.desc)
