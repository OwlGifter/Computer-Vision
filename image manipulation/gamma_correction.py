import numpy as np
import cv2 as cv

cv.destroyAllWindows()

img0 = cv.resize(np.float32(cv.imread('./image manipulation/ac1.png')/255),(720,400))
img1 = cv.resize(np.float32(cv.imread('./image manipulation/webcam.jpg')/255),(720,400))
img2 = cv.resize(np.float32(cv.imread('./image manipulation/shadow road.jpg')/255),(720,400))

images = [img0,img1,img2]
images= [img/np.max(img) for img in images]

# Gamma correction
for i, img in enumerate(images):
    for gamma in [1, 0.8,0.6,0.4]:
        cv.imshow(f"Image {i}, {gamma =  :.1f} ", img**gamma)
cv.waitKey()
