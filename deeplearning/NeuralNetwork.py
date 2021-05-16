# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:12:09 2021

Common neural network
@author: liyunlong
@date 2021-05-16
"""
import numpy as np

class NeuralNetwork:
    '神经网络框架'
    rate = 0.01;
    def __init__(self, level):
        # 记录是第几层
        self.level = level;

    """
    x：输入x
    w：训练参数w
    """    
    def learn(self, x, w):
        z = np.dot(w, x);
        print(z);
        a = 1 / (1 + np.exp(-z));
        print(a);

x = np.arange(1,9).reshape(2,4);
w = np.array([1,1,2,2]).reshape(2,2);
print(x);
print(w);
        
nw = NeuralNetwork(1);
nw.learn(x, w);
    

            