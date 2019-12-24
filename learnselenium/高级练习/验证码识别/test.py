#coding=utf-8
'''
使用图像识别第三方库
'''
import tesserocr
from PIL import Image
#print(tesserocr.tesseract_version())  # print tesseract-ocr version
#print(tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('code.jpg')
print(tesserocr.image_to_text(image))  # print ocr text from image
# 第二种识别方法
print(tesserocr.file_to_text('code.jpg'))