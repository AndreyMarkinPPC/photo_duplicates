import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,

                    help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                    help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

winSize = (20,20)
blockSize = (10,10)
blockStride = (5,5)
cellSize = (10,10)
nbins = 6
derivAperture = 1
winSigma = -1.0
histogramNormType = 0
L2HysThreshold = 0.2
gammaCorrection = 1
nlevels = 4
useSignedGradients = True
 
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,\
                         cellSize,nbins,derivAperture,winSigma, \
                         histogramNormType,L2HysThreshold,gammaCorrection, \
                         nlevels, useSignedGradients)
img = cv2.imread(args["images"])
dim = (int(img.shape[0] * 0.1), int(img.shape[1] * 0.1))
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
descriptor = hog.compute(img)
print(np.round(descriptor, 4))
# print("shape of descriptor: ", descriptor.shape)
