import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def retinex(img, sigma=30):
    """
    对图像应用 Retinex 算法进行增强，并在每一步操作后展示图像结果。
    :param img: 输入的彩色图像
    :param sigma: 高斯模糊的标准差，控制尺度
    :return: 增强后的图像
    """
    # 转换为浮点型并加 1
    img = img.astype(np.float32) + 1.0
    
    # 计算对数图像
    img_log = np.log(img)

    # 应用高斯模糊来模拟照明成分
    blurred = cv.GaussianBlur(img_log, (0, 0), sigma)

    # 计算反射成分
    result = img_log - blurred
    result = np.exp(result) - 1.0
    plt.subplot(2, 3, 3)
    plt.imshow(cv.cvtColor(np.uint8(result), cv.COLOR_BGR2RGB))
    plt.title('Retinex Result')
    plt.axis('off')

    # 归一化并转换为 uint8
    result = cv.normalize(result, None, 0, 255, cv.NORM_MINMAX)
    result = np.uint8(result)
    return result

# # 读取图像
# image_path = 'images/text1.jpg'
# image = cv.imread(image_path)

# # 应用 Retinex 算法
# retinex_image = retinex(image)

# # 显示原始图像和处理后的图像
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
# plt.title('Original Image')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(cv.cvtColor(retinex_image, cv.COLOR_BGR2RGB))
# plt.title('Retinex Enhanced Image')
# plt.axis('off')

# plt.show()

# # 保存处理后的图像
# cv.imwrite('images/new_text1.jpg', retinex_image)
