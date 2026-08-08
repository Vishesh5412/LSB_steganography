# LSB Steganography CLI

A lightweight, high-performance command-line tool written in Python to securely hide and extract secret text messages inside images using Least Significant Bit (LSB) steganography.

---
## Installation & Setup

Run the following commands in your terminal to clone the repository, set up a virtual environment, and install the package:

```bash
git clone [https://github.com/Vishesh5412/LSB_steganography.git](https://github.com/Vishesh5412/LSB_steganography.git)
cd LSB_steganography
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Usage

### 1. Hide Text
Embeds a secret text message inside an image file.

**Syntax:**
```bash
hide_text <image_path> "<text_message>"
````
Note: Make sure to wrap text_message in double quotes.

### 2. Show Text
Extracts and displays the original text hidden inside an image.

**Syntax:**
```bash
show_text <image_path>
