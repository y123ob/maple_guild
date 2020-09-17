import cv2
import numpy as np

file_make_mode = False

def col_2_num(col):
    mul = [[1],[2],[4],[8],[16],[32],[64],[128],[256],[512],[1024],[2048]]
    val = sum(col * mul) // 255
    return val[0]

def make_chr_db(img, x, y, size_x, size_y, unicode_number):
    new_img = img[y:y+size_y,x:x+size_x]
    return [chr(unicode_number)] + [col_2_num(new_img[0:size_y,i:i+1]) for i in range(size_x)]


if file_make_mode:
    file = open('hangul.txt', 'w', encoding='UTF-8')
    for i in range(0xAD00, 0xD800):
        file.write(chr(i))
    for i in range(128):
        file.write(chr(i))
else:
    img = cv2.imread('han.png', cv2.IMREAD_GRAYSCALE)
    file = open('han_db.txt', 'w', encoding='UTF-8')
    start_unicode = 0xAD00
    start_image_x = 1
    start_image_y = 43

    for i in range(74):
        for j in range(146):
            this_unicode = start_unicode + j + 146 * i
            x = start_image_x + 13 * j
            y = start_image_y + 13 * i
            data = make_chr_db(img, x, y, 12, 12, this_unicode)
            data = str(data)
            file.write(data + '\n')

    for j in range(10917-10805):
        this_unicode = start_unicode + j + 146 * 74
        x = start_image_x + 13 * j
        y = start_image_y + 13 * 74
        data = make_chr_db(img, x, y, 12, 12, this_unicode)
        data = str(data)
        file.write(data + '\n')
    
    ascii_code = 33
    x = 2
    y = start_image_y + 13 * 75
    size_x = 0
    for j in range(2,700):
        if col_2_num(img[y:y+12, j:j+1]) != 4095:
            size_x+=1
        else:
            if j == 5:
                size_x+=1
                continue
            else:
                if(size_x == 0):
                    x+=1
                    continue
                data = make_chr_db(img, x, y, size_x, 12, ascii_code)
                ascii_code += 1
                data = str(data)
                file.write(data + '\n')
                x = x + size_x + 1
                size_x = 0