import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# Painting the image
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=4)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (100,250), (300,400), (255,0,0), thickness=4)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Hey Vsauce! Michael Here.', (100, 225), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
