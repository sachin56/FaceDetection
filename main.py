import cv2

img = cv2.imread('franke.jpg', 1)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2*2)))


cv2.imshow("legend", resized)
cv2.waitKey(0)


cv2.destroyAllWindows()

print(img.shape)
