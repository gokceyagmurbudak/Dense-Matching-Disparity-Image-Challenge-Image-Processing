import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm

min_disp = 0
max_disp = 256 
# Maximum disparity minus minimum disparity. The value is always greater than zero.
# In the current implementation, this parameter must be divisible by 16.
num_disp = max_disp - min_disp 
blockSize = 7
imgL = cv.imread('im1.png',0)
imgR = cv.imread('im2.png',0)
stereo = cv.StereoSGBM_create(minDisparity= min_disp,
    numDisparities = num_disp,
    # Matched block size. It must be an odd number >=1 . Normally, it should be somewhere in the 3..11 range.
    blockSize = 7,
    # Normally, a value within the 5-15 range is good enough, but I prefered zero because of the error ratio.(when I used 5-15 , I got more error ratio )
    uniquenessRatio = 0,
    # Maximum size of smooth disparity regions to consider their noise speckles and invalidate.
    # Set it to 0 to disable speckle filtering. Otherwise, set it somewhere in the 50-200 range.
    speckleWindowSize = 50,
     #Maximum disparity variation within each connected component.
     # If you do speckle filtering, set the parameter to a positive value, it will be implicitly multiplied by 16.
     # Normally, 1 or 2 is good enough.I used 32 because of the error ratio.(when I used 1 or 2 , I got more error ratio )
    speckleRange = 32,
    disp12MaxDiff = 300,
    P1 = 8*blockSize**2,
    P2 =32*blockSize**2)
disparity = stereo.compute(imgL,imgR)

#normalize the resulting values to a range of 0...255 so that they can be directly shown and saved as a grayscale image.
disparity = cv.normalize(disparity, disparity, alpha=255,
                              beta=0, norm_type=cv.NORM_MINMAX)
disparity = np.uint8(disparity)
plt.imshow(disparity,'gray')
plt.show()
plt.imsave('output.png', disparity, cmap = cm.gray)