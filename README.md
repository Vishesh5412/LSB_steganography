# ️ LSB Steganography CLI

A lightweight, high-performance command-line tool written in Python to securely hide and extract secret text messages inside images using Least Significant Bit (LSB) steganography.

---

## Usage
1. Hide Text
Embeds a secret text message inside an image file.

Syntax:
hide_text <image_path> "<text_message>" # [Make sure to wrap text_message inside double quotes.]


2. Show Text
Show the original text hidden inside image.

Syntax:
show_text <image_path> 
