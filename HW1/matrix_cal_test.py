import numpy as np
from . import *

A = [[3, 4],
    [-2, 4]]
B = [[2, 0],
    [1, -2]]

result_add, result_sub = matrix_add_and_sub(A, B)

test_add = np.array(
    [[5, 4],
    [-1, 2]]
)
if np.array_equal(result_add, test_add):
    print('행렬 덧셈 계산이 맞았습니다.')
else:
    print('행렬 덧셈 계산이 틀렸습니다.')

test_sub = np.array(
    [[1, 4],
    [-3, 6]]
)
if np.array_equal(result_sub, test_sub):
    print('행렬 뺄셈 계산이 맞았습니다.')
else:
    print('행렬 뺄셈 계산이 틀렸습니다.')

result_mul = matrix_mul(A, B)

test_mul = np.array(
    [[10, -8],
    [0, -8]]
)
if np.array_equal(result_mul, test_mul):
    print('행렬 곱셈 계산이 맞았습니다.')
else:
    print('행렬 곱셈 계산이 틀렸습니다.')