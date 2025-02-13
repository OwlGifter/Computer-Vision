import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as nd

#gray image of the cars as well as normal image
img = plt.imread('./Filtering exercise/cars1500.png')
img_gray = img[:,:,0]*.299 + img[:,:,1]*.587 + img[:,:,2]*.114
plt.imshow(img_gray,cmap='gray')
plt.title("image in gray")
plt.show()
plt.imshow(img)
plt.title("normal image")
plt.show()

#Box Filtering with sizes 1,3,7,15,31
print("Convolve from scipy")
size = [1,3,7,15,31]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

for i, s in enumerate(size):
  f = np.ones((s,s))
  f = f/np.sum(f)
  img_f = nd.convolve(img_gray,f)
  ax[i].imshow(img_f,cmap='gray')
  ax[i].set_title('Convolve scipy, size= '+str(s))
plt.show()

#same thing using filter from scipy
print("Uniform_filter from scipy")
size = [1,3,7,15,31]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

for i, s in enumerate(size):
  img_f = nd.uniform_filter(img_gray,s)
  ax[i].imshow(img_f,cmap='gray')
  ax[i].set_title('Uniform filter, size= '+str(s))
plt.show()


#gaussean filter
print("Gaussian filter from scipy")
size = [.1,1,10,100]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

for i, s in enumerate(size):
  img_f = nd.gaussian_filter(img_gray,s)
  ax[i].imshow(img_f,cmap='gray')
  ax[i].set_title('Gaussian filter, size= '+str(s))
plt.show()


#Prewitt edge detector
print("Prewitt filter from scipy")
size = [0,1]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

for i, s in enumerate(size):
  img_f = nd.prewitt(img_gray, axis= s)
  ax[i].imshow(img_f,cmap='gray')
  ax[i].set_title('Prewitt filter, axis= '+str(s))
plt.show()


#Sobel edge detector
print("Sobel filter from scipy")
size = [0,1]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

for i, s in enumerate(size):
  img_f = nd.sobel(img_gray, axis= s)
  ax[i].imshow(img_f,cmap='gray')
  ax[i].set_title('Sobel filter, axis= '+str(s))
plt.show()


#Sharpen Image
print("Sharpening image")
size = [1,2]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

for i, s in enumerate(size):
  blurred_img = nd.gaussian_filter(img_gray,s)
  blurrier_img = blurred_img - img_gray
  alpha = 1
  sharpened_img = img_gray - alpha * blurrier_img

  ax[i].imshow(sharpened_img, cmap='grey')
  ax[i].set_title('Sharpening, strength= '+str(s))
plt.show()

#Box filtering color
print("Convolve filter - Color")
size = [1,3,7,15,31]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

filteredImg = np.copy(img)
for i, s in enumerate(size):
  f = np.ones((s,s))
  f = f/np.sum(f)
  filteredImg[:,:,0] = nd.convolve(filteredImg[:,:,0],f)
  filteredImg[:,:,1] = nd.convolve(filteredImg[:,:,1],f)
  filteredImg[:,:,2] = nd.convolve(filteredImg[:,:,2],f)
  ax[i].imshow(filteredImg)
  ax[i].set_title('Convolve-Color, size= '+str(s))
plt.show()

#gaussean filter on color
print("Gaussean filter - Color")
size = [.1,1,10,100]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

filteredImg = np.copy(img)
for i, s in enumerate(size):
  filteredImg[:,:,0] = nd.gaussian_filter(filteredImg[:,:,0],s)
  filteredImg[:,:,1] = nd.gaussian_filter(filteredImg[:,:,1],s)
  filteredImg[:,:,2] = nd.gaussian_filter(filteredImg[:,:,2],s)
  ax[i].imshow(filteredImg)
  ax[i].set_title('Gaussean-Color, size= '+str(s))
plt.show()

#Prewitt edge detector color
print("Prewitt edge - Color")
size = [0,1]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

filteredImg = np.copy(img)
for i, s in enumerate(size):
  filteredImg[:,:,0] = nd.prewitt(filteredImg[:,:,0],s)
  filteredImg[:,:,1] = nd.prewitt(filteredImg[:,:,1],s)
  filteredImg[:,:,2] = nd.prewitt(filteredImg[:,:,2],s)
  ax[i].imshow(filteredImg)
  ax[i].set_title('Prewitt-Color, axis= '+str(s))
plt.show()

#Sobel edge detector color
print("Sobel edge -Color")
size = [0,1]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

filteredImg = np.copy(img)
for i, s in enumerate(size):
  filteredImg[:,:,0] = nd.sobel(filteredImg[:,:,0],s)
  filteredImg[:,:,1] = nd.sobel(filteredImg[:,:,1],s)
  filteredImg[:,:,2] = nd.sobel(filteredImg[:,:,2],s)
  ax[i].imshow(filteredImg)
  ax[i].set_title('Sobel-Color, axis= '+str(s))
plt.show()

#Sharpen image with color
print("Sharpen img - Color")
size = [1,2,3]
fig, ax = plt.subplots(1,len(size),figsize=(28, 12))

filteredImg = np.copy(img)
for i, s in enumerate(size):

  # blurred_img = nd.gaussian_filter(img_gray,s)
  # blurrier_img = blurred_img - img_gray
  # alpha = 30
  # sharpened_img = img_gray - alpha * blurrier_img

  filteredImg[:,:,0] = nd.gaussian_filter(filteredImg[:,:,0],s)
  filteredImg[:,:,1] = nd.gaussian_filter(filteredImg[:,:,1],s)
  filteredImg[:,:,2] = nd.gaussian_filter(filteredImg[:,:,2],s)


  filteredImg[:,:,0] -= img[:,:,0]
  filteredImg[:,:,1] -= img[:,:,1]
  filteredImg[:,:,2] -= img[:,:,2]

  alpha = .3
  sharpened_img = img - alpha * filteredImg
  ax[i].imshow(sharpened_img)
  ax[i].set_title('Sharpening-Color, Strength= '+str(s))
plt.show()