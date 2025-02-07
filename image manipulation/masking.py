import numpy as np
import cv2 as cv

cv.destroyAllWindows()

img0 = cv.resize(np.float32(cv.imread('./image manipulation/ac1.png')/255),(720,400))
img1 = cv.resize(np.float32(cv.imread('./image manipulation/webcam.jpg')/255),(720,400))
img2 = cv.resize(np.float32(cv.imread('./image manipulation/shadow road.jpg')/255),(720,400))

images = [img0,img1,img2]
images= [img/np.max(img) for img in images]

# Creating binary mask      
mask = np.zeros((400,720,1))
mask[100:300,180:540] =  1
cv.imshow("Mask", mask)

for i, img in enumerate(images):
    cv.imshow("Masked image "+str(i), img*mask)
    cv.imshow("Masked image "+str(i) +' v2', img*(1-mask))

# Combining masked images
for i in range(3):
    j = (i+1)%3
    cv.imshow(f"Combined masked images {i} and {j} ", images[i]*mask+images[j]*(1-mask))

cv.waitKey()