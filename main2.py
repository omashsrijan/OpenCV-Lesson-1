import cv2
#Render image in grayscale
img=cv2.imread("C:/Users/Srikanth Mashetty/Desktop/Opencv Lesson 1/pikachu.png", 0)
#imshow is used to show loaded image in window with title
cv2.imshow("Grandpa Pika Pic", img)

#to hold output until key is pressed:
cv2.waitKey(0)
#to delete process when Key is pressed:
cv2.destroyAllWindows()