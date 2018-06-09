import tornado.web

from utils import account
from .main import AuthBaseHandler

class LoginHandler(AuthBaseHandler):

    def get(self):
        if self.current_user:
            self.redirect('/')
        self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        passed = account.authenticate(username, password)

        if passed:
            self.session.set('user_info', username)
            account.login(username)
            self.redirect('/')
        else:
            self.write('login fail')

class LogoutHandler(AuthBaseHandler):
    def get(self):
        self.session.set('user_info', '')
        self.redirect('/login')

class SignupHandler(AuthBaseHandler):
    def get(self):
        self.render('signup.html',
                    msg='')

    def post(self, *args, **kwargs):
        username=self.get_argument('username', None)
        email= self.get_argument('email', None)
        password1=self.get_argument('password1', '')
        password2 = self.get_argument('password2', '')
        if username and password1 and password2 and email:
            if password1 != password2:
                self.write({'msg': '两次密码不匹配'})
            else:
                ret = account.redister(username, password1, email)
                if ret['msg'] == 'ok':
                    self.session.set('user_info', username)
                    self.redirect('/')
                else:
                    self.write(ret)

        else:
            self.render('signup.html',
                        msg={'register fail'}
                        )