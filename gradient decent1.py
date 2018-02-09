# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:27:19 2018

@author: Shabnam Rani
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import random

def SampleGenerating(n, divergence=100):
    X = np.matrix(range(n)).T + 1
    Y = np.matrix([random.random() *divergence + i * 10 + 900 for i in range(len(X))]).T
    return X, Y

def modelgradientfitting(x, y):
    N = len(x)
    w = np.zeros((x.shape[1], 1))
    
    learningrate=0.0001

    iterations = 50
    for i in range(iterations):
        error = x * w - y
        print("error")
        print(error)
        gradient = x.T * error / N
        w = w - learningrate * gradient
    return w

def plotting(x, y, w):
    plt.plot(x[:,1], y, "x")
    plt.plot(x[:,1], x * w, "r-")
    plt.show()

def test(n, divergence, modelFunction):
    X, Y = SampleGenerating(n, divergence)
    X = np.hstack([np.matrix(np.ones(len(X))).T, X])
    w = modelFunction(X, Y)
    plotting(X, Y, w)


test(50, 600, modelgradientfitting)
test(150, 100, modelgradientfitting)
test(100, 200, modelgradientfitting)



