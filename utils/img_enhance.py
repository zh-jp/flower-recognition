import cv2
import numpy as np


'''
在训练卷积神经网络之前，进行图像增强可以提高模型的泛化能力和鲁棒性。图像增强可以通过多种方式实现，例如裁剪、旋转、平移、缩放、颜色变换等。
通过这些增强技术，可以增加训练集的多样性，使得模型能够更好地学习到图像的不同变换和变化。
这有助于减少过拟合现象，并且可以提高模型的鲁棒性，使得模型在处理新的、未见过的图像时也能够表现良好。
总之，在训练卷积神经网络之前，进行图像增强是一个非常有用的步骤，可以提高模型的泛化能力和鲁棒性，从而提高模型的性能和效果。
'''


# 调整亮度和对比度
def imgAdjust(img):
    alpha = 1.5 # 调整亮度和对比度的倍数
    beta = 10
    img_adjust = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return img_adjust


# 图像旋转
def imgRotate(img):
    angle = 45 # 旋转角度
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1) # 获得旋转矩阵
    img_rotate = cv2.warpAffine(img, M, (cols, rows)) # 执行旋转操作
    return img_rotate


# 图像平移
def imgTranslate(img):
    tx, ty = 50, 30 # 平移距离
    M = np.float32([[1, 0, tx], [0, 1, ty]]) # 获得平移矩阵
    rows, cols = img.shape[:2]
    img_translate = cv2.warpAffine(img, M, (cols, rows)) # 执行平移操作
    return img_translate


# 图像裁剪
def imgCrop(img):
    rows, cols = img.shape[:2]
    x = int(cols * 0.2)
    w = int(cols * 0.6)
    y = int(rows * 0.2)
    h = int(rows * 0.6)
    # x, y, w, h = 100, 100, 200, 200 # 裁剪区域的左上角坐标和宽高
    img_crop = img[y:y+h, x:x+w]
    return img_crop


# 图像缩放
def imgResize(img):
    fx, fy = 0.5, 0.5 # 缩放比例
    img_resize = cv2.resize(img, None, fx=fx, fy=fy)
    return img_resize


# 颜色变换
def imgColor(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # 转换为HSV颜色空间
    h, s, v = cv2.split(img_hsv) # 分离颜色通道
    v = cv2.equalizeHist(v) # 直方图均衡化亮度通道
    img_hsv = cv2.merge((h, s, v)) # 合并颜色通道
    img_color = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR) # 转换回BGR颜色空间
    return img_color


if __name__ == "__main__":
    # 读取图像
    img = cv2.imread('D:/1670211885840.jpeg')
    # 显示图像
    cv2.imshow('Original', img)
    # cv2.imshow('Adjust', imgAdjust(img))
    # cv2.imshow('Rotate', imgRotate(img))
    # cv2.imshow('Translate', imgTranslate(img))
    cv2.imshow('Crop', imgCrop(img))
    # cv2.imshow('Resize', imgResize(img))
    # cv2.imshow('Color', imgColor(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
