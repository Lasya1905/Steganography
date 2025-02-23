import cv2
import os
import string

image = cv2.imread('encryptedImg.png')

message_length = int(input('Enter Length of Message: '))
og_passcode = input('Enter Original Passcode: ')
passcode = input('Enter Passcode: ')

c = {}
d = {}

for i in range(255):
    d[chr[i]] = i
    c[i] = chr(i)

if passcode == og_passcode:
    message = ''
    n = 0 
    m = 0
    z = 0
    for i in range(message_length):
        message = c[image[n,m,z]]+message
        n +=1
        m +=1
        z = (z+1)%3

        print('Decrytion Message: '+message)
else:
    print('You are not Authorized.')