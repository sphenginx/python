#! /usr/local/bin/python3

'''
本次实现把 一张图片 切割为 九宫格 图片
'''

# -*- coding: utf-8 -*-
import os
from PIL import Image

def cut_image(image):
    width, height= image.size
    item_width = width /3.0
    item_height = height /3.0
    box_list = []
    for row in range(0, 3):
        for col in range(0, 3):
            box = (col * item_width, row * item_height,( col +1) * item_width,( row +1) * item_height)
            box_list.append(box)

    imagelist = [image.crop(box) for box in box_list]
    return imagelist


def save_images(imagelist):
    dirname = 'output'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    index = 1
    for image in imagelist:
        image.save('./output/python'+ str(index) +'.png', 'PNG')
        index +=1

if __name__ == '__main__':
    image = Image.open("use.png")
    imagelist = cut_image(image)
    save_images(imagelist)
