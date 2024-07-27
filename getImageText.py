from PIL import Image
import pytesseract
import cv2 as cv
import os
import imageProcess

# 指定 Tesseract OCR 引擎的路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Linux 路径
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract-python\tesseract.exe'  # Windows 路径

def extractImageText(image_path):
    # image_path = os.path.abspath(image_path)
    # 打开图像文件
    cv_image = cv.imread(image_path)
    if cv_image is None:
        raise ValueError(f"无法加载图像，请检查路径是否正确: {image_path}")
    # 使用retinex算法处理
    processed_image = imageProcess.retinex(cv_image)
    # openCV图像格式转换成PIL.Image格式
    final_image = Image.fromarray(cv.cvtColor(processed_image, cv.COLOR_BGR2RGB))
    # 使用 Tesseract OCR 进行文字识别
    text = pytesseract.image_to_string(final_image, lang='eng+chi_sim')  # 'eng+chi_sim' 支持英文和简体中文
    # 去除图片中可能的分行
    tmp_text = text.split('\n')
    final_text = ''
    # 遍历split函数后的数组
    for i in range(len(tmp_text)):
        final_text += tmp_text[i]
    # 返回识别出的文字
    return final_text
