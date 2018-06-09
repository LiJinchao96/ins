from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'ins'
USERNAME = 'admin'
PASSWORD = 'Root110qwe'

Db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    PORT,
    DATABASE
)

engine=create_engine(Db_url)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base(engine)