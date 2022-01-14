import os
from PIL import Image
arr = os.listdir('F:\Downloads\pokevision')
#print(arr)
for im in arr:
    im1 = Image.open(r'F:\Downloads\pokevision\\' + im)
    im1.save(r'F:\Downloads\pokevision\\' + im.replace(".jpg","") + '.png')
#!rm *.jpg
