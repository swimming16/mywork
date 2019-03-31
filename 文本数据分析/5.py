import os
import glob
from PIL import Image
def fun(path):
    a=glob.glob('*.jpg')
    print(a)
    for s in a:
        name=os.path.join(path,s)
        #print(name)
        im=Image.open(name)
        im.thumbnail((500, 300))
        print(im.format,im.size,im.mode)
        im.save(name+'1','JPEG')
if __name__=='__main__':
    path='.'
    fun(path)
