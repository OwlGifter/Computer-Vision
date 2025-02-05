import numpy as np
import cv2 as cv
import time

camera = 0 
start = time.time()
cap = cv.VideoCapture(camera)
cap.set(3,1280) # Set number of columns in captured image to 1280
cap.set(4,720) # Set number of columns in captured image to 1280
elapsed_time = time.time()-start
print(f'Initializing camera {camera} took {elapsed_time:.2f} seconds')

count = 0
start = time.time()

while True:

    count+=1

    ok, img = cap.read()
    if not ok:
        print('Error reading image')
        break
    # img = cv.resize(img, (1280,720))      if img is too big
    # cv.imshow('Image',img)
    # img[:,:,:2] = 0   to turn it into red img
    redImg = np.copy(img)
    redImg[:,:,:2] = 0
    cv.imshow('Red Channel',redImg)
    img = img[:,::-1,:]
    cv.imshow('Flipped',img)
    
    k = cv.waitKey(1) # if character 'q' is pressed, exit
    if k == ord('q'):
        break

elapsed_time = time.time()-start
print(f'Image shape: {img.shape}')
print(f'Captured {count} frames')
print(f'Capture speed: {count/elapsed_time:.2f} frames per second')
cap.release()
cv.destroyAllWindows()
