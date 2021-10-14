import numpy as np

def matrix_mul(matrix_A: list, matrix_B: list) -> np.array:
    A_array = np.array(matrix_A)
    B_array = np.array(matrix_B)

    mul = np.dot(A_array, B_array)

    return mul