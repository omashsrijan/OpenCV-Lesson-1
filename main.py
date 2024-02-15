import cv2
#IMREAD_COLOR makes pic renders the image in color
img=cv2.imread("C:/Users/Srikanth Mashetty/Desktop/Opencv Lesson 1/pikachu.png", cv2.IMREAD_COLOR)
#imshow is used to show loaded image in window with title
cv2.imshow("Pika Pic", img)

#to hold output until key is pressed:
cv2.waitKey(0)
#to delete process when Key is pressed:
cv2.destroyAllWindows()