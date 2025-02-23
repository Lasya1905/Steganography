# StegaPyX - Image-Based Steganography Tool

StegaPy is a simple yet effective steganography tool that allows users to hide and retrieve secret messages inside images using Least Significant Bit (LSB) encoding. The tool is built using Python and provides a graphical user interface (GUI) using Tkinter.

## Features
- **Hide a secret message** within an image.
- **Retrieve the hidden message** using a passcode.
- **Simple and user-friendly GUI** for easy operation.
- Supports **PNG, JPG, and JPEG** image formats.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Required Libraries
Run the following command to install the required dependencies:
```bash
pip install opencv-python numpy pillow tkinter
```

## Usage
### Running the Application
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/Lasya1905/Steganography.git
cd StegaPy
```
Run the Python script:
```bash
python stegap.py
```

### Encrypting a Message
1. Click **"Select Image"** and choose an image file.
2. Enter the **secret message** you want to hide.
3. Set a **password** to protect the message.
4. Click **"Encrypt"** to embed the message into the image.
5. The encrypted image will be saved as `encryptedImage.png`.

### Decrypting a Message
1. Click **"Select Image"** and choose the encrypted image.
2. Enter the **password** used during encryption.
3. Click **"Decrypt"** to retrieve the hidden message.

## File Structure
```
StegaPy/
│── stegap.py  # Main application script
│── README.md  # Project documentation
│── requirements.txt  # List of dependencies (optional)
```

## Contributing
Feel free to submit issues or pull requests to improve this project.

