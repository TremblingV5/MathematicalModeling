'''
    linear programming
    Used package: scipy, numpy
'''

'''
    The model of this code is :
    max:    z = 2x1 + 3x2 - 5x3
    s.t.:   x1 + x2 + x3 = 7
            2x1 - 5x2 +x3 >= 10
            x1 + 3x2 + x3 <= 12
            x1 >= 0
            x2 >= 0
            x3 >= 0
'''
from scipy import optimize as op
import numpy as np

c = np.array([2, 3, -5])

A_ub = np.array([[-2, 5, -1],[1, 3, 1]])
B_ub = np.array([10, 12])

A_eq = np.array([[1, 1, 1]])
B_eq = np.array([7])

x1 = (0, None)
x2 = (0, None)
x3 = (0, None)

res = op.linprog(-c, A_ub, B_ub, A_eq, B_eq, bounds=(x1, x2, x3))

print(res)