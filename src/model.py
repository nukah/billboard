from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime

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
    name = Column(String)
    place = Column(String)
    date = Column(DateTime)
    desc = Column(String)
    
    def __init__(self, name, place, date, text = None):
        self.name = name
        self.place = place
        self.date = date
        self.desc = text or ''
        
    def __repr__(self):
        return "<Event('%s','%s','%s','%s','%s')>" % (self.id, self.name, self.place, self.date, self.text)