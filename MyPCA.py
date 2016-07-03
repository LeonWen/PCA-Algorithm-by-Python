# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:45:57 2016

@author: LeonWen
"""

import os

from PIL import Image
from numpy import *
from pylab import *


path = r'D:\Projects\PythonProj\ImageProcessing\2012'
sst_dir = os.listdir(path)
file_len = len(sst_dir)

sst_list = []

for i in range(file_len):
    str = path + '\\' + sst_dir[i]
    #txt = open(str).read()
    sst_list.append(str)

immatrix = []

for im in sst_list:
    text = loadtxt(im)    
    immatrix.append(text)

immatrix = array(immatrix)

# 显示输出
figure()
gray()
for i in range(file_len):
    subplot(3,4,i + 1)
        
    pic = immatrix[i].reshape(180,360)
    pic = pic[::-1]
#    picshow = rot90(pic,4)
    imshow(pic)
    colorbar()
    
show()

# 转换成样本总体
X = immatrix.T
# 获取要本大小
m,n = X.shape[0:2]

# 取得各个样本均值
meanVal = mean(X,axis = 0)
#tempMean = tile(meanVal,(64800,1))

# 样本矩阵去中心化
X = X - tile(meanVal,(64800,1))

# 计算协方差
S = dot(X.T,X) / (m - 1)

# 计算特征值eg和特征向量Ev
eg,Ev = linalg.eig(S)
#eg1,Ev1 = linalg.eigh(S) # 这两种算法的结果还不一样，返回结果的排序区别，eigh返回结果由小到大
'''
    这个返回的特征矩阵与Matlab返回的结果不一致，大小相似但是却出现正负值的差异
    特征值大小一致
'''

# 计算新的成分
Y = dot(immatrix.T,Ev)

figure()
gray()
for i in range(n):
    subplot(3,4,i + 1)
    out = Y[:,i]
#    min_num = min(out)
#    max_num = max(out)
    
    outpic = out.reshape(180,360)
    outpic = outpic[::-1]
#    outpic = rot90(outpic)    
    imshow(outpic)
#    imshow(outpic,vmin = min_num,vmax = max_num)
    colorbar()
    
show()










