'''
    linear programming
    Used package: scipy, numpy
'''


'''
    The model of this code is :
    max:    z = 4x1 + 3x2
    s.t.:   2x1 + x2 <= 10
            x1 + x2 <= 8
            x2 <= 7
            x1 >= 0
            x2 >= 0
'''
from scipy import optimize as op
import numpy as np
'''
    First, set a target function, the number of list is arguments of target function.
'''
c=np.array([4, 3])

'''
    Second, set unequal relations.
    The number of list of A_ub is arguments of constraint function, if unequal relation is "<=", use primary arguments.
    If not, use arguments*-1.
    
    The number of list of B_ub is value of constraint function.
'''
A_ub=np.array([[2, 1],[1, 1],[0, 1]])
B_ub=np.array([10, 8, 7])

'''
    Third, set equal relations, just like the second step.
'''
# A_eq=np.array([[1,1,1]])
# B_eq=np.array([7])

'''
    Forth, set range of x, None means infinity
'''
x1=(0,None)
x2=(0,None)

'''
    Fifth, use op.linprog to access answer, if target function need a max value, should use "-c", if not, use "c"
'''
res=op.linprog(-c,A_ub,B_ub,bounds=(x1,x2))

print(res)
'''
    The output of last line is:
             con: array([], dtype=float64)
             fun: -25.999999999841208
         message: 'Optimization terminated successfully.'
             nit: 5
           slack: array([8.02664601e-11, 3.92610389e-11, 1.00000000e+00])
          status: 0
         success: True
               x: array([2., 6.])
               
    In this lines, two of the most important lines is "fun" and "x"
    "fun" means the answer of question, if you need a max value, fun*-1
    "x" means corresponding value of x1, x2, x3 ......
'''