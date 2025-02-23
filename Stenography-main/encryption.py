import cv2
import os
import string

img = cv2.imread('mypic.png')

message = input('Enter Message: ')
passcode = input('Enter Passcode: ')

c = {}
d = {}
for i in range(255):
    # converting to ASCII Values
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in message:
    img[n,m,z] = d[message[i]]
    n +=1
    m +=1
    z = (z+1)%3

cv2.imwrite('encrytedImg.png',img)
os.system('start encryptedImg.png')

