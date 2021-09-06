import cv2
import numpy as np
print("Package Imported")

img = cv2.imread("Resources/Devil.jpg")
print(img.shape)
imgResize = cv2.resize(img, (400, 400)) # 1st width and 2nd height
print(imgResize.shape)

imgCropped = img[0:200, 200:500] # 1st height and 2nd width

cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)