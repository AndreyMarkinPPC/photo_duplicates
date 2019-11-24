import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                    help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                    help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

def check_blur(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


img = cv2.imread(args['images'])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = check_blur(gray)
print(blur)
