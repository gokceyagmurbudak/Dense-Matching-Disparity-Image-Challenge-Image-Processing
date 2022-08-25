import cv2 as cv

img_disparity = cv.imread("output.png",0)
img_gtdisp = cv.imread("GTdisp_im1.png",0)

counter_corresponse = 0
counter_not = 0


#The pixel values were checked with 1 pixel value precision.
for i in range (1110):
    # the image started with 255 and end with 1390 because of the stereo situation.
    for j in range (255,1390):
        if img_gtdisp[i][j] != 0 :
            if (img_disparity[i][j] == img_gtdisp[i][j] or
             img_disparity[i][j] == img_gtdisp[i][j] +1 or
             img_disparity[i][j] == img_gtdisp[i][j] -1):
                counter_corresponse += 1
            else:
                counter_not += 1
                
#error_ratio_2 = counter_corresponse / counter_not

zero_pixels = 0
# Pixel values of 0 have been extracted in the Gtdisp_im1.png image.
for i in range (1110):
    for j in range (255,1390):
        if img_gtdisp[i][j] == 0 :
            zero_pixels += 1
            
            


total_pixels = 1110*(1390-256) - zero_pixels

accuracy_ratio = (counter_corresponse / total_pixels)*100

print("accuracy ratio %", accuracy_ratio)
# Output: accuracy ratio % 70.75278264793863
