import numpy as np
import cv2 as cv
import time

def channel(img,c):
    #returns correct channel based on c value
    if(c == 0):
        return img[:,:,0:1]
    if(c == 1):
        return img[:,:,1:2]
    if(c == 2):
        return img[:,:,2:]
    return img

def gray(img):
    #gets the average of channels combined, then saves answer in every channel
    img[:,:,:] = (img[:,:,0:1] + img[:,:,1:2] + img[:,:,2:])/3
    return img

def red(img):
    img[:,:,0:2] = 0
    return img

def green(img):
    #sets blue and red channel to zero individually
    img[:,:,0:1] = 0
    img[:,:,2:] = 0
    return img

def blue(img):
    img[:,:,1:] = 0
    return img

def swapped(img):
    #changes color order with a -1 step
    img = img[:,:,::-1]
    return img

def mirror(img):
    img = img[:,::-1,:]
    return img

def upside_down(img):
    img = img[::-1,:,:]
    return img

def zoom(img,r0=None,c0=None,height=None, width=None):
    if r0==None: r0 = img.shape[0]//4
    if c0==None: c0 = img.shape[1]//4
    if height==None: height = img.shape[0]//2
    if width==None: width = img.shape[1]//2
    #makes camera look only at set height and width and then resizes it to regular size
    return cv.resize(img[r0:r0+height,c0:c0+width, :],(1280,720))

def highlighted(img,r0=None,c0=None,height=None, width=None,gamma=0.75):
    if r0==None: r0 = img.shape[0]//4
    if c0==None: c0 = img.shape[1]//4
    if height==None: height = img.shape[0]//2
    if width==None: width = img.shape[1]//2
    #makes the set area brighter by dividing area by gamma
    img[r0:r0+height,c0:c0+width,:] = img[r0:r0+height,c0:c0+width,:]/gamma
    return img

def motion(img,prev_img):
    if(prev_img is None):
        return img
    #for motion it just returns the difference between current and past image, has to be positive
    difference = np.abs(img -prev_img)
    return difference

def blended(img,prev_img,alpha=0.95):
    #multiplies prev image by .95, then adds the current image multiplied by .5, for transition to be slow
    img = prev_img*alpha + img*.05
    return img

def mask(img,mask):
    #sets area to be multiplied by the 0/1 mask
    img[:168,:300,:] = img[:168,:300,:] * mask   #sets the exact size of the image to multiply by the mask
    return img

def mask_full(img,mask):
    #resizes image
    mask = cv.resize(mask, (img.shape[1],img.shape[0]))
    #creates temporary mask with 3 channels
    maskTemp = np.ones((720,1280,3))
    #sets all channels equal to the mask in the respective spot
    for i in range(3):
        maskTemp[:,:,i] = mask
    #multiplies image by mask with 3 channels
    return img * maskTemp

def brightest(img):
    #iterates through entire photo to find brightest, then outputs that
    brightestL = (0,0)
    brightness = -1
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            tempBrightness = sum(img[r,c])
            if tempBrightness > brightness:
                brightness = tempBrightness
                brightestL = (r,c)
    c,r = brightestL
    return cv.rectangle(img, (r-20,c-20), (r+20,c+20),(0,255,0),2)

if __name__ == "__main__":
    camera = 0
    start = time.time()
    cap = cv.VideoCapture(camera)
    cap.set(3,1920)
    cap.set(4,1080)
    #cap.set(3,1280)
    #cap.set(4,720)
    elapsed_time = time.time()-start
    print(f'Initializing camera {camera} took {elapsed_time:.2f} seconds')

    print("Press any of the following characters")
    print("\"n\" normal image read from the camera")
    print("\"y\" gray level version of image")
    print("\"0\" blue channel of image")
    print("\"1\" greeb channel of image")
    print("\"2\" red channel of image")
    print("\"r\" red version of image")
    print("\"g\" green version of image")
    print("\"b\" blue version of image")
    print("\"s\" swapped-channel version of image")
    print("\"m\" mirrored version of image")
    print("\"u\" upside-down version of image")
    print("\"e\" blended version of image")
    print("\"z\" zoomed version of image") 
    print("\"h\" highlighted version of image")
    print("\"t\" motion version of image")
    print("\"x\" image with overlaid box surrounding brightest pixel")
    print("\"k\" image with overlaid binary mask on top-left corner")
    print("\"l\" image with overlaid binary mask, with mask scaled to image size")
    print("\"w\" to save to a file the image being displayed")
    print("\"q\" to quit the program")

    out_dir = '.\\frames\\'
    count = 0
    frame_count = 0
    start = time.time()
    f = 0
    last_key = 'n'
    prev_img = 0
    logo = 1-np.float32(cv.imread('./Lab 1/utep_logo_bw.png')[:,:,0:1])/255
    
    # Uncomment to see the UTEP logo
    #cv.imshow('Logo',logo)

    while True:

        count+=1
        
        ok, img_in = cap.read()
        
        if not ok:
            print('Error reading image')
            break
        img_in = cv.resize(np.float32(img_in)/255, (1280, 720))
        
        k = cv.waitKey(1) 
        if k>=0:
            prev_key = last_key
            last_key = chr(k)

        if last_key == 'q':
            break

        elif last_key == 'w':
            outfile = out_dir+'frame'+str(1000+frame_count)[1:]+'.jpg'
            cv.imwrite(outfile,np.uint8(img_out*255))
            print(f'saved frame {frame_count} to {outfile}')
            last_key = prev_key
            frame_count+=1

        elif last_key in '012':
            img_out = channel(img_in,int(last_key))

        elif last_key == 'n':
            img_out = img_in
            
        elif last_key == 'y':
            img_out = gray(img_in)

        elif last_key == 'r':
            img_out = red(img_in)

        elif last_key == 'g':
            img_out = green(img_in)

        elif last_key == 'b':
            img_out = blue(img_in)

        elif last_key == 's':
            img_out = swapped(img_in)
            
        elif last_key == 'm':
            img_out = mirror(img_in)

        elif last_key == 'u':
            img_out = upside_down(img_in)

        elif last_key == 'z':
            img_out = zoom(img_in)

        elif last_key == 'h':
            img_out = highlighted(img_in)

        elif last_key == 'e':
            img_out = blended(img_in,prev_img,alpha=0.95)
            prev_img = img_out

        elif last_key == 't':
            img_out = motion(img_in,prev_img)
            prev_img = img_in

        elif last_key == 'x':
            img_out = brightest(img_in)

        elif last_key == 'k':
            img_out = mask(img_in,logo)

        elif last_key == 'l':
            img_out = mask_full(img_in,1-logo)

        else:
            img_out = img_in

        cv.imshow('Image',img_out)
            

    elapsed_time = time.time()-start
    print(f'Image shape: {img_out.shape}')
    print(f'Captured {count} frames')
    print(f'Capture speed: {count/elapsed_time:.2f} frames per second')
    cap.release()
    cv.destroyAllWindows()

