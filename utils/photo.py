import glob
import os
from PIL import Image

def get_images(path):
    images=[]
    for file in glob.glob(path+'/*.jpg'):
        images.append(file)
    return images

def make_thumb(path):
    dirname = os.path.dirname(path)
    file, ext = os.path.splitext(os.path.basename(path))
    im = Image.open(path)
    im.thumbnail((200, 200))
    save_thumb_to = os.path.join(dirname, 'thumbs', '{}_{}x{}.jpg'.format(file, 200, 200))
    im.save(save_thumb_to, "JPEG")
    #return save_thumb_to