'''
    linear programming
    Assignment problem
    Used package: scipy, numpy
'''
import numpy as np
from scipy.optimize import linear_sum_assignment

'''
    First, set a efficiency matrix
'''
efficiency_matrix = np.array([
    [12,7,9,7,9],
    [8,9,6,6,6],
    [7,17,12,14,12],
    [15,14,6,6,10],
    [4,10,7,10,6]
])

'''
    Second, return the best row and col
'''
row_index, col_index = linear_sum_assignment(efficiency_matrix)

print(row_index+1)
'''
    The last line will print the best row
'''

print(col_index+1)
'''
    The last line will print the best col
'''
print(efficiency_matrix[row_index,col_index])

print(efficiency_matrix[row_index, col_index].sum())