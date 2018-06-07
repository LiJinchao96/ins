import tornado.web
import os
from utils import photo



class IndexHandler(tornado.web.RequestHandler):
    """
    Home page for use,photo feeds
    """
    def get(self):
        images_path= os.path.join(self.settings.get('static_path'), 'uploads')
        images = photo.get_images(images_path)
        self.render('index.html',
                    images = images)

class ExploreHandler(tornado.web.RequestHandler):
    def get(self):
        thumbs_path = os.path.join(self.settings.get('static_path'), 'uploads/thumbs')
        image_urls = photo.get_images('./static/uploads/thumbs')
        self.render('explore.html',
                    images=image_urls,
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
                with open('./static/uploads/'+img_file['filename'], 'wb') as f:
                    f.write(img_file['body'])
                photo.make_thumb('./static/uploads/'+img_file['filename'])

        else:
            self.write({'msg':'empty form'})

        self.write({'msg': 'got file:{}'.format(img_files[0]['filename'])})


