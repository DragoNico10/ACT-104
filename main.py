import cv2
import tkinter.messagebox
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img=cv2.imread('solar-system.jpg')
cv2.putText(img, 'Sun', (100,80), font, 2, (27,111,237))
cv2.putText(img, 'Mercury', (110,250), font, 0.7, (127,125,128))
cv2.putText(img, 'Venus', (170,180), font, 1, (23,101,174))
cv2.putText(img, 'Earth', (270,270), font, 1, (149, 74, 63))
cv2.putText(img, 'Moon', (315,160), font, 0.5, (213, 213, 213))
cv2.putText(img, 'Mars', (365,270), font, 1, (55, 79, 137))
cv2.putText(img, 'Jupiter', (480, 50), font, 2, (88, 132, 191))
cv2.putText(img, 'Saturn', (740,320), font, 1.5, (143, 167, 202))
cv2.putText(img, 'Uranus', (950, 300), font, 1, (236, 233, 195))
cv2.putText(img, 'Neptune', (1090, 300), font, 1, (220, 86, 58))
cv2.imshow('ACT-104',img)

if tkinter.messagebox.askyesno('ACT-104','Save image?'):
    cv2.imwrite('solar-system(with text).jpg', img)
    tkinter.messagebox.showinfo('ACT-104', 'Image saved!')
cv2.waitKey(0)