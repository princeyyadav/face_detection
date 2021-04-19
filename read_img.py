import cv2

img = cv2.imread("dog.jpg")
cv2.imshow("Dog's Image", img)

gray = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Dog's Image in Gray", gray)

print(gray.shape, img.shape)

cv2.waitKey(0) # wait infinitely
cv2.destroyAllWindows()