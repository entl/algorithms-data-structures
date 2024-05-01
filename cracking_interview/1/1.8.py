# Zero Matrix: Write an algorithm such that
# if an element in an MxN matrix is 0, its entire
# row and column are set to 0.
from typing import List
import pandas as pd


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    row_list = []
    col_list = []
    width = len(matrix)
    height = len(matrix[0])

    for row in range(width):
        for col in range(height):
            if matrix[row][col] == 0:
                row_list.append(row)
                col_list.append(col)

    for row in row_list:
        nullify_row(matrix, row)

    for col in col_list:
        nullify_col(matrix, col)

    print(pd.DataFrame(matrix))
    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def test_zero_matrix():
    matrix = [
        [1, 2, 3],
        [4, 0, 1],
        [7, 8, 9]
    ]
    test = [
        [1, 0, 3],
        [0, 0, 0],
        [7, 0, 9]
    ]

    assert zero_matrix(matrix) == test


if __name__ == "__main__":
    test_zero_matrix()
    print("1.8.py: All tests passed")