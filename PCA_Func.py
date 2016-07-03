# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:33:32 2015

@author: LeonWen

Direction: PCA algorithm from <Programming Computer Vision with Python>
"""

from PIL import Image
from numpy import *

def pca(X):
    """主成分分析：
    输入:矩阵X，其中该剧真中存在训练数据，每一行为一条训练数据
    返回:投影矩阵（按照维度的重要性排序）、方差和均值
    """
    
    # 获取维数
    num_data,dim = X.shape
    
    # 数据中心化
    mean_X = X.mean(axis = 0)
    X = X - mean_X
    
    if dim > num_data:
        # PCA - 使用紧致技巧？#################不是很懂这个意思###########
        M = dot(X,X.T) # 协方差矩阵
        e,EV = linalg.eigh(M) # 特征值和特征向量
        tmp = dot(X.T,EV).T # 此处为紧致技巧 ###########################
        V = tmp[::-1] # 由于最后的特征向量才是我们所需要的，故将其逆转
        S = sqrt(e)[::-1] # 由于特征值是按递增顺序排列，故需要将其逆转
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        # PCA - 使用SVD方法
        U,S,V = linalg.svd(X)
        V = V[:num_data] # 返回前num_data维的数据
        
    # 返回投影矩阵、方差和均值
    return V,S,mean_X
    
        
    