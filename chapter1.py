import cv2
print("Package Imported")

img = cv2.imread("Resources/Devil.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)