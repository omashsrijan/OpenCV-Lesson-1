import cv2
#Render image in grayscale
img=cv2.imread("C:/Users/Srikanth Mashetty/Desktop/Opencv Lesson 1/pikachu.png", 0)
#imshow is used to show loaded image in window with title
cv2.imshow("Grandpa Pika Pic", img)
#imwrite is used to write image to folder(directory)
cv2.imwrite("pika.png", img)
print("Successfully saved")
#to hold output for 5 seconds and then delete process:
cv2.waitKey(0)
cv2.destroyAllWindows()