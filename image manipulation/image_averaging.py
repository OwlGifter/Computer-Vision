import numpy as np
import cv2 as cv

cv.destroyAllWindows()
    
img0 = cv.resize(np.float32(cv.imread('./image manipulation/ac1.png')/255),(720,400))
img1 = cv.resize(np.float32(cv.imread('./image manipulation/webcam.jpg')/255),(720,400))
img2 = cv.resize(np.float32(cv.imread('./image manipulation/shadow road.jpg')/255),(720,400))

images = [img0,img1,img2]

# Displaying original images
for i, img in enumerate(images):
    cv.imshow("Image "+str(i), img)

# Scaling so maximum value in array is 1 to lighten dark images
images_s= [img/np.max(img) for img in images]
for i, img in enumerate(images_s):
    cv.imshow("Image scaled "+str(i), img)

# Averaging images
w0 = 0.5
w1 = 1-w0 # w0+w1 must be equal to 1
for i in range(3):
    j = (i+1)%3
    cv.imshow(f"Average of images {i} and {j} ", w0*images_s[i]+w1*images_s[j])

# Smooth transition from one image to another by slowly changing weights
i,j = 2,0
for w1 in np.linspace(0,1,100):
    w0 = 1 - w1
    cv.imshow(f"Transition from  {i} and {j} ", w0*images_s[i]+w1*images_s[j])
    cv.waitKey(50) # Wait for 50 ms
cv.waitKey()