import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
array = np.random.rand(207,9)*100
#print(array)

A = np.random.rand(10)*10

def f(z, A):
    A = np.asarray(A)
    idx = (np.abs(A - z)).argmin()
    return A[idx]

img1 = misc.face()
misc.imsave('face.png', img1) 
img2 = misc.face(gray=True)
plt.imshow(img1)
plt.show()
plt.imshow(img2, cmap=plt.cm.gray)
plt.show()
plt.imshow(img2, cmap=plt.cm.gray, vmin=10, vmax=200)

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

for c, ax in zip(range(3), axs):
    tmp_im = np.zeros(img1.shape, dtype="uint8")
    tmp_im[:,:,c] = img1[:,:,c]
    ax.imshow(tmp_im)
    ax.set_axis_off()
plt.show()

def grayscale(im, weights = np.c_[0.2989, 0.5870, 0.1140]):
    tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
    return np.sum(tile * im, axis=2)

gsimg = grayscale(img1)
plt.imshow(gsimg, cmap='Greys')