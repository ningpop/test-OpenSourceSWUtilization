import numpy as np

def matrix_add_and_sub(matrix_A: list, matrix_B: list) -> tuple:
    A_array = np.array(matrix_A)
    B_array = np.array(matrix_B)

    add = A_array + B_array
    sub = A_array - B_array

    return (add, sub)