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
    def __init__(self, deep, weight, rate):
        self.deep = deep; #深度
        self.weight = weight; #权重或参数
        self.rate = rate; #学习率

    def learn(self):
        a = np.array(self.deep);
        for i in range(self.deep):
            a[i] = np.exp(i) * self.rate;
            
        print(a);
    
nw = NeuralNetwork(3, 0, 0.01);

nw.learn();
            