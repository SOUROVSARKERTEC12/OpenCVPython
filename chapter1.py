import cv2
import numpy as np
print("Package Imported")

img = cv2.imread("Resources/Devil.jpg")
print(img.shape)
imgResize = cv2.resize(img, (400, 400))

cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.waitKey(0)