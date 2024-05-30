#1/usr/bin/env python3
'''
gradient descent with L2
'''


import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Updates the weights and biases of a neural network using gradient
    descent with L2 regularization
    """
    m = Y.shape[1]
    A = cache[f'A{L}']
    dA_prev = A - Y

    for i in reversed(range(1, L + 1)):
        A_prev = cache[f'A{i-1}'] if i > 1 else cache['A0']
        W = weights[f'W{i}']
        b = weights[f'b{i}']

        dZ = dA_prev
        dW = (1 / m) * np.dot(dZ, A_prev.T) + (lambtha / m) * W
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)
        dA_prev = np.dot(W.T, dZ) * (1 - np.square(A_prev))

        weights[f'W{i}'] = W - alpha * dW
        weights[f'b{i}'] = b - alpha * db

