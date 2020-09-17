import cv2
import numpy as np

def col_2_num(col):
    mul = [[1],[2],[4],[8],[16],[32],[64],[128],[256],[512],[1024],[2048]]
    val = sum(col * mul) // 255
    return val[0]

def img_2_txt(img, db, size = 12):
    img_height, img_width = img.shape()
    img_col_lis = [col_2_num(img[0:size, i:i+1]) for i in range(img_width)]
    st = 0 ; ed = 1
    while(ed <= len(img_col_lis)):
        if(img_col_lis[ed] == 0 or  ed == len(img_col_lis)):
            try:
                idx = db.index(img_col_lis[st:ed])
                
            except:
                idx = -1
            