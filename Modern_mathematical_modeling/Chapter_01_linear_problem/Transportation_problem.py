'''
    linear programming
    Transportation problem
    Used package: pulp, numpy
'''
import pulp
import numpy as np
from pprint import pprint

def transportation_problem(costs, x_max, y_max):
    '''
    :param costs: an array contains every items cost
    :param x_max: constraint value of x
    :param y_max: constraint value of y
    :return:
    '''

    row = len(costs)
    col = len(costs[0])

    '''
        First, init a problem named "prob", sense means what we want to get, "LpMaximize" means we want a max value
    '''
    prob = pulp.LpProblem('Transportation Problem', sense=pulp.LpMaximize)

    '''
        Second, set constraint value, lowBound means the lowest permitted value, cat means type of value
    '''
    var = [[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpInteger) for j in range(col)] for i in range(row)]

    '''
        Third, set constraint function
    '''
    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

    prob += pulp.lpDot(flatten(var), costs.flatten())

    for i in range(row):
        prob += (pulp.lpSum(var[i]) <= x_max[i])

    for j in range(col):
        prob += (pulp.lpSum([var[i][j] for i in range(row)]) <= y_max[j])

    prob.solve()

    return {'objective':pulp.value(prob.objective), 'var': [[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]}

if __name__ == '__main__':
    costs = np.array([[500, 550, 630, 1000, 800, 700],
                       [800, 700, 600, 950, 900, 930],
                       [1000, 960, 840, 650, 600, 700],
                       [1200, 1040, 980, 860, 880, 780]])

    max_plant = [76, 88, 96, 40] # x
    max_cultivation = [42, 56, 44, 39, 60, 59] # y
    res = transportation_problem(costs, max_plant, max_cultivation)

    print(f"最大值为{res['objective']}")
    print('各变量的取值为：')
    pprint(res['var'])