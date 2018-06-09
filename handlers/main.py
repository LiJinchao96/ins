import tornado.web
import os
from pycket.session import SessionMixin
from utils import photo, account

class AuthBaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return self.session.get('user_info')

class IndexHandler(AuthBaseHandler):
    """
    Home page for use,photo feeds
    """
    @tornado.web.authenticated
    def get(self):
        posts = account.get_post_for(self.current_user)
        image_urls = [p.image_url for p in posts]
        self.render('index.html',
                    images = image_urls)

class ExploreHandler(AuthBaseHandler):
    def get(self):
        posts = account.get_post_for(self.current_user)
        thumb_urls = [p.thumb_url for p in posts]
        self.render('explore.html',
                    images=thumb_urls,
                    )

class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        self.render('post.html',
                    post_id=post_id,
                    )

class UploadHandler(tornado.web.RequestHandler ):
    def get(self):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        img_files = self.request.files.get('pic', None)
        if img_files:
            for img_file in img_files:
                image_url = 'uploads/' + img_file['filename']
                save_to = os.path.join(self.settings['static_path'], image_url)
                print("save to   {}".format(save_to))
                with open(save_to, 'wb') as f:
                    f.write(img_file['body'])
                photo.make_thumb(save_to)
                full_path = photo.make_thumb(save_to)
                thumb_url = os.path.relpath(full_path, self.settings['static_path'])
                account.add_post_for(self.current_user, image_url, thumb_url)

            self.write({'filename': img_files[0]['filename']})
            self.redirect('/explore')

        else:
            self.write({'msg':'empty form'})

        self.write({'msg': 'got file:{}'.format(img_files[0]['filename'])})


