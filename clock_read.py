
import cv2
import numpy

up_img=cv2.imread("clock_pic.jpg",1)
up_img=cv2.resize(up_img,(500,500))
img=cv2.cvtColor(up_img, cv2.COLOR_BGR2GRAY)
img=cv2.bitwise_not(img)
(_,cnts,_)=cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in cnts:
    if cv2.contourArea(contour) < 1000 or cv2.contourArea(contour) > 7000:
        continue
    (x,y,w,h)= cv2.boundingRect(contour)
    cv2.rectangle(up_img, (x,y), (x+w, y+h), (0,255,0), 3)
rotrect = cv2.minAreaRect(contour)
#im2=cv2.drawContours(rotrect, cnts, -1, (0,255,0), 3)  
cv2.imshow("test", up_img)

key=cv2.waitKey(0)
cv2.destroyAllWindows()