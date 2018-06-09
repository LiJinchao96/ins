import hashlib
from datetime import datetime
from models.user_modules import User, session


def hash_it(password):
    return hashlib.md5(password.encode('utf8')).hexdigest()

def authenticate(username, password):
    if username and password:
        hash_password = User.get_pass(username)
        if hash_password and hash_it(password) == hash_password:
            return True

    return False

def login(username):
    t = datetime.now()
    print("user: {} login at {}".format(username,t))
    user_query = session.query(User).filter(User.name==username)
    user_query.update({User.last_login: t})
    session.commit()


def redister(username, password, email):

    if User.is_exists(username):
        return {'msg': 'username is exists'}

    hash_pass = hash_it(password)
    User.add_user(username, hash_pass, email)
    return {'msg': 'ok'}
