import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

## OpenCV is used for loading, modifying and saving image 
## PIL is used for resizing and displaying image in Tkinter


def open_image():
    global img, img_path, tk_image
    
    # user selects image using filedialog.askopenfilename()
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        # if image path exists, image is read.
        img = cv2.imread(img_path)
        pil_img = Image.open(img_path)
        pil_img = pil_img.resize((250, 250))
        tk_image = ImageTk.PhotoImage(pil_img) # resized version of window is displayed
        img_label.config(image=tk_image) # used to update img_label widget
        img_label.image = tk_image # prevents GC from removing it

def encrypt_message():
    global img
    if img is None:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    msg = msg_entry.get()

    global password
    password = pass_entry.get()
    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 2
        z = (z + 1) % 3
    
    encrypted_path = "encryptedImage.png"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")
    messagebox.showinfo("Success", "Message encrypted and saved as encryptedImage.png")

def decrypt_message():
    global img
    if img is None:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    entered_pass = pass_entry.get()
    global password
    if password != entered_pass:
        messagebox.showerror("Error", "Incorrect password!")
        return
    
    c = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    decrypted_msg = ""
    
    for i in range(len(msg_entry.get())):
        decrypted_msg += c[img[n, m, z]]
        n += 1
        m += 2
        z = (z + 1) % 3
    
    messagebox.showinfo("Decrypted Message", f"Message: {decrypted_msg}")

root = tk.Tk() # to create main window, we use Tk() class
root.title("Steganography Tool")
root.geometry("400x500")

img_label = tk.Label(root, text="No Image Selected", width=30, height=10)
# refers to display box. master->root(parameter to represent parent window)

img_label.pack()

tk.Button(root, text="Select Image", command=open_image).pack()
# master -> root

tk.Label(root, text="Enter Message:").pack()
msg_entry = tk.Entry(root, width=40) # Single line text input
msg_entry.pack()

tk.Label(root, text="Enter Password:").pack()
pass_entry = tk.Entry(root, width=40, show="*") # Single line text input
pass_entry.pack()

tk.Button(root, text="Encrypt", command=encrypt_message).pack()
tk.Button(root, text="Decrypt", command=decrypt_message).pack()

root.mainloop() # method used to run the application once it is ready. 
                # creates infinite loop.
