import cv2
import numpy as np
import argparse
import glob
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True,
	help="path to input folder")
ap.add_argument("-o", "--output", type=str, required=True,
    help="path to output folder")
args = vars(ap.parse_args())

def cut(img):
  # crop image
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
  morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

  cnts, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnt = sorted(cnts, key=cv2.contourArea)[-1]
  x,y,w,h = cv2.boundingRect(cnt)
  new_img = img[y:y+h, x:x+w]
 # cv2.imshow("cut", new_img)
  return new_img

def transBg(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
  morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

  roi, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  mask = np.zeros(img.shape, dtype=img.dtype)


  cv2.fillPoly(mask, roi, (255,)*img.shape[2], )
  masked = cv2.bitwise_and(img, mask)


  return masked


def fourChannels(img):
  height, width, channels = img.shape
  if channels < 4:
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    return new_img

  return img

def cropImg(img):
    s_img = cv2.imread(img)
    print("cropping " + img)
    # set to 4 channels
    s_img = fourChannels(s_img)

    # remove white background
    s_img = cut(s_img)

    # set background transparent
    s_img = transBg(s_img)
    print("writing to " + args["output"] + img.split("\\")[-1])
    cv2.imwrite( args["output"] + "\\" + img.split("\\")[-1], s_img )

for file in glob.glob(args["input"] + "\\*.png"):
        cropImg(file)
