import numpy as np
import cv2 as cv


img0 = cv.resize(np.float32(cv.imread('./exercise 1/ac1.png')/255),(720,400))
img1 = cv.resize(np.float32(cv.imread('./exercise 1/webcam.jpg')/255),(720,400))
img2 = cv.resize(np.float32(cv.imread('./exercise 1/shadow road.jpg')/255),(720,400))

cv.imshow("Image 0", img0)
cv.imshow("Image 1", img1)
cv.imshow("Image 2", img2)

print(np.min(np.mean(img0,axis=-1)),np.max(np.mean(img0,axis=-1)))
cv.imshow("Image 0b", img0/np.max(np.mean(img0,axis=-1)))
cv.imshow("Image 1b", img1/np.max(np.mean(img1,axis=-1)))
cv.imshow("Image 2b", img2**.4)
cv.waitKey(0)