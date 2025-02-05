import numpy as np
import cv2 as cv

def GrnRemover(img):
    img[:,:,1:2] = 0      #sets green to 0
    img[:,:,0] = 1-img[:,:,0] #reverses blue
    return img
def turnToMask(img):
    mask = img/255
    mask[:,:,2] /=.5   #increases red value due to red being mostly in the figure
    mask[:,:,:]= (mask[:,:,0:1]+mask[:,:,1:2]+mask[:,:,2:])/3 #averages blue and red values
    mask = np.clip(mask,.3,.4) #sets values to be .3 lowest, and .4 highest
    mask = mask-.3
    mask = mask*10 #vales should mostly be either 0 or 1

    mask = mask[:,:,2]
    mask[mask < .5] = 0
    mask[mask >=.5] = 1 #ensures there is only 0 or 1 in the array
    mask = np.reshape(mask, (np.shape(mask)[0],np.shape(mask)[1],1)) #turns 2d array into a 3d array
    return mask

img0 = cv.imread('./quiz 2/quixote.jpg')
img1 = cv.imread('./quiz 2/windmills.jpg')

# cv.imshow("quixote", img0)    #317,233
# cv.imshow("windmills", img1)  #500x333     to put image at bottom left it should mask at "183x100"
mask = np.copy(img0)
mask = GrnRemover(mask)
mask = turnToMask(mask)

#sets img0 background to black
img0 = np.float32(img0/255)
img0 = img0*mask

#sets img1 silouhette to black
img1 = np.float32(img1/255)
img1[100:,183:,:] *= 1-mask

#adds the img0 with a black background to the img1 with the black silouhette
img1[100:,183:,:] += img0


# cv.imshow("img0", img0)
cv.imshow("mask", mask)
cv.imshow("flipped mask", 1-mask)
cv.imshow("Answer", img1)
cv.waitKey(0)