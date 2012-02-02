"""DOCUMENTATION TODO"""
from settings import settings
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
engine = create_engine(settings['database_cred'], echo=False)
from sqlalchemy.ext.declarative import declarative_base
from utils.hasher import *

Base = declarative_base()

class User(Base):
    
    """DOCUMENTATION TODO"""
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    email = Column(String(75), nullable=True)
    password = Column(String(128), nullable=False)
    account_type = Column(String(128), nullable=True) #Twitter, Facebook, or Local
    details = Column(String(1000), nullable=True)

def __repr__(self):
    return "<User('%s')>" % (self.username)

users_table = User.__table__
metadata = Base.metadata

def get_user(db, username=None, email=None, user_id=None):
    if username!=None:
        return db.query(User).filter_by(username=username).first()
    if email !=None:
        return db.query(User).filter_by(email=email).first()
    if id != None:
        return db.query(User).filter_by(user_id=user_id).first()
    raise Exception('You didnt give any non-None arguments')
    

def create_user(username,email, password, account_type='Local', details=''):
    new_user = User()
    new_user.username = username
    new_user.email = email
    new_user.password = pass_hash(password)
    new_user.account_type=account_type
    new_user.details = details
    return new_user



def create_all():
    """DOCUMENTATION TODO"""
    metadata.create_all(engine)

def drop_all():
    """DOCUMENTATION TODO"""
    metadata.drop_all(engine)
    

def commit(db, objs):
    for obj in objs:    
        logging.info(obj)
        db.add(obj)

    db.commit()

    