import cv2
#Render image in grayscale
img=cv2.imread("C:/Users/Srikanth Mashetty/Desktop/Opencv Lesson 1/pikachu.png", 1)
# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged
#Spilitting pika.png into different saturations of R, G, and B
B,G,R=cv2.split(img)

cv2.imshow("original", img)
cv2.waitKey(delay=5000)
cv2.destroyWindow("original")

cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(delay=5000)
cv2.destroyWindow("Blue Saturation Image")

cv2.imshow("Green Saturation Image", G)
cv2.waitKey(delay=5000)
cv2.destroyWindow("Green Saturation Image")

cv2.imshow("Red Saturation Image", R)
cv2.waitKey(delay=5000)
cv2.destroyWindow("Red Saturation Image")