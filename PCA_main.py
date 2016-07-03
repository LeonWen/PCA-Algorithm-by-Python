# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:35:54 2015

@author: LeonWen

"""

# 读取文件列表
import os

from PIL import Image
from numpy import *
from pylab import *
import PCA_Test

'''
testpath = 'D:\\URDoingYourLoving\\sst_pic\\1.tif'
img = Image.open(testpath)
img.show()
'''

path = 'D:\\URDoingYourLoving\\sst_pic'
im_dir = os.listdir(path)
len_num = len(im_dir)
i = 0
imlist = []
for i in im_dir:
    imlist[i] = path + r'\\' + im_dir[i]
    i += 1

str = imlist[0]

im = array(Image.open(str)) # 先获取一幅图像，得到图像尺寸信息
m,n = im.shape[0:2]

'''
imnbr = len(imlist)

# 创建矩阵，将图像转为一维数据
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')
'''