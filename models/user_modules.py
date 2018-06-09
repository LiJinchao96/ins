from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey 
from .db import Base, session
from sqlalchemy.sql import exists
from sqlalchemy.orm import relationship 

class User(Base):
    __tablename__= 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    password = Column(String(50),nullable=False)
    creates = Column(DateTime, default=datetime.now)
    email = Column(String(50))
    last_login = Column(DateTime)

    def __repr__(self):
        return '<users>(id={},name={})'.format(self.id, self.name)

    @classmethod
    def is_exists(cls, username):
        return session.query(exists().where(User.name==username)).scalar()


    @classmethod
    def add_user(cls, username, password, email=''):
        user = User(name=username, password=password,
                    email=email, last_login=datetime.now())
        session.add(user)
        session.commit()

    @classmethod
    def get_pass(cls, username):
        user = session.query(cls).filter(User.name==username).first()
        if user:
            return user.password
        else:
            return ' '
        
class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(80))
    thumb_url = Column(String(80))
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship('User', backref='posts', uselist=False, cascade='all')

    def _repr_(self):
        return "<Post(#{})>".format(self.id) 

if __name__== '__main__':
    Base.metadata.create_all()