import cv2
import sys
import os

    
def hide_text():
    if (len(sys.argv) != 3):
        print("Error, Enter valid command!!")
        return

    path_to_img = sys.argv[1]
    str = sys.argv[2]

    if not os.path.exists(path_to_img):
        print("Error, Enter a valid path!!")
        return

    img = cv2.imread(path_to_img)
    if img is None:
        print("Error, Enter a valid image!!")
        return

    str += "\0"
    h, w, c = img.shape
    c_idx = 0
    for c in str:
        ascii_str = format(ord(c), '08b')    
        ascii_idx = 0

        while ascii_idx != 8:
            c_row = int (c_idx / w)
            c_col = c_idx % w
            for j in range(3):
                if (ascii_idx == 8): 
                    break
                img[c_row, c_col, j] = img[c_row, c_col, j] >> 1
                img[c_row, c_col, j] = (img[c_row, c_col, j] * 2 + 1) if (ascii_str[ascii_idx] == '1') else (img[c_row, c_col, j] * 2)
                ascii_idx = ascii_idx + 1

            c_idx = c_idx + 1

    base_name = os.path.basename(path_to_img)
    file_name_only, extension = os.path.splitext(base_name)

    cv2.imwrite(f"output_{file_name_only}.png", img) 

def show_text():
    if (len(sys.argv) != 2):
        print("Error, Enter valid command!!")
        return
    
    path_to_img = sys.argv[1]
    
    if not os.path.exists(path_to_img):
        print("Error, Enter a valid path!!")
        return

    img = cv2.imread(path_to_img)
    if img is None:
        print("Error, Enter a valid image!!")
        return

    decoded_message = ""
    h, w, c = img.shape
    c_idx = 0

    while c_idx != h * w:
        ascii_str = ""
        for i in range(3):
            c_row = int (c_idx / w)
            c_col = c_idx % w
            for j in range(3):
                if (len(ascii_str) == 8):
                    break
                ascii_str += ('1' if (img[c_row, c_col, j] & 1) else '0')
            c_idx = c_idx + 1
        decoded_char = chr(int(ascii_str, 2))
        if (decoded_char == "\0"):
            print(decoded_message)
            return
        decoded_message += decoded_char

    print(decoded_message)


