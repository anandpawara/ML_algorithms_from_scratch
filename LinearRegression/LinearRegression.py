################################ Tutorial Link ##########################
#         https://www.youtube.com/watch?v=ltXSoduiVwY&t=61s             #
#########################################################################

# Steps:
# Training:
#     1. Initialize weght as zero
#     2. Initialize biase as zero

# Given a data point:
#     1. Predict result by using y-hat = wx + b
#     2. Calculate error
#     3. Use gradient descent to figure out new weight and bais values`
#     4. Repeat n times

import numpy as np

class LinearRegression:
    
    def __init__(self, lr = 0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape()
        self.weights = np.zeros()
    
    def predict():
        pass