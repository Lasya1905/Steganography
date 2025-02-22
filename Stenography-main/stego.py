import cv2
import os
import string


img = cv2.imread("mypic.png") # Replace with the correct image path: to read the image

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {} # maps characters to ascii values
c = {} # maps ascii values to charcaters

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)


# n,m,z are used to update the pixels
m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
