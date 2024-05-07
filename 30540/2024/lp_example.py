import numpy as np
from scipy.optimize import linprog

'''
ex 7.2 DPV

decision variables: kn, kc, mn, mc
'''
print('\nDPV 7.2\n')
# objective
c = np.array([2, 3, 4, 1])

A_ub = np.array([\
[-1, 0,-1, 0],\
[ 0,-1, 0,-1],\
[ 1, 1, 0, 0],\
[ 0, 0, 1, 1],\
])
# b_ub = 
b_ub = np.array([-10, -13, 15, 8])

bounds = []
for i in range(len(c)):
    bounds.append((0, None))

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(result)

'''
ex 7.8 DPV

decision variables: z, a, b
'''
print('\nDPV 7.8\n')
p = [(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)]

# objective
c = np.array([1, 0, 0])

A_ub = np.array([\
[-1, p[0][0], 1],\
[-1, p[1][0], 1],\
[-1, p[2][0], 1],\
[-1, p[3][0], 1],\
[-1, p[4][0], 1],\
[-1, p[5][0], 1],\
[-1, p[6][0], 1],\
[-1, -p[0][0], -1],\
[-1, -p[1][0], -1],\
[-1, -p[2][0], -1],\
[-1, -p[3][0], -1],\
[-1, -p[4][0], -1],\
[-1, -p[5][0], -1],\
[-1, -p[6][0], -1],\
])
# b_ub = 
b_ub = np.array([\
    p[0][1], p[1][1], p[2][1], p[3][1], p[4][1], p[5][1], p[6][1], \
    -p[0][1], -p[1][1], -p[2][1], -p[3][1], -p[4][1], -p[5][1], -p[6][1] ])

bounds = []
for i in range(len(c)):
    bounds.append((0, None))

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(result)

'''
ex 7.10  DPV

decision variables:
sa, sb, sc, ad, ab, ae, be, cb, cf, de, dg, eg, ef, gt, ft
'''
print('\nDPV 7.10\n')
# objective
c = np.array([-1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# capacities
A_ub = np.identity(15)
b_ub = np.array([6, 1, 10, 4, 2, 1, 20, 2, 5, 2, 5, 10, 6, 12, 4])

# conservation laws
A_eq = np.array([\
# sa, sb, sc, ad, ab, ae, be, cb, cf, de, dg, eg, ef, gt, ft
[  1,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0],\
[  0,  1,  0,  0,  1,  0, -1,  1,  0,  0,  0,  0,  0,  0,  0],\
[  0,  0,  1,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0],\
[  0,  0,  0,  1,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0],\
[  0,  0,  0,  0,  0,  1,  1,  0,  0,  1,  0, -1, -1,  0,  0],\
[  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0, -1],\
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0, -1,  0]\
])
b_eq = np.zeros(7)

bounds = []
for i in range(len(c)):
    bounds.append((0, None))

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
print(result)

'''
ex 7.12 DPV

'''
print('\nDPV 7.12\n')

# primal
c_p = np.array([-1, 2, 0])
A_ub = np.array([[1, -1, 0],[ 0,2, -1]])
b_ub = np.array([1,1])
bounds = []
for i in range(len(c_p)):
    bounds.append((0, None))

result = linprog(c_p, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(result)

# dual
c_p = np.array([1, 1])
A_ub = np.array([[-1, 0],[ 1,-2],[0,1]])
b_ub = np.array([-1,2,0])
bounds = []
for i in range(len(c_p)):
    bounds.append((0, None))

result = linprog(c_p, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(result)

'''
ex 7.25  DPV
max flow
decision variables:
sa, sb, ab, at, bt
'''
print('\nDPV 7.25 max flow\n')
# objective
c = np.array([-1, -1, 0, 0, 0])

# capacities
A_ub = np.identity(5)
# b_ub = np.array([6, 1, 10, 4, 2, 1, 5, 2, 5, 2, 5, 5, 6, 12, 4])
b_ub = np.array([1, 3, 1, 2, 1])

# conservation laws
A_eq = np.array([\
# sa, sb, ab, at, bt
[  1,  0, -1, -1,  0],\
[  0,  1,  1,  0, -1],\
])
b_eq = np.zeros(2)

bounds = []
for i in range(len(c)):
    bounds.append((0, None))

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
print(result)

print('\nDPV 7.25 min cut\n')
# objective
c = np.array([1, 3, 1, 2, 1, 0, 0])

# capacities
A_ub = np.array([\
[-1, 0, 0, 0, 0,-1, 0],\
[ 0,-1, 0, 0, 0, 0,-1],\
[ 0, 0,-1, 0, 0, 1,-1],\
[ 0, 0, 0,-1, 0, 1, 0],\
[ 0, 0, 0, 0,-1, 0, 1],\
])
# b_ub = np.array([6, 1, 10, 4, 2, 1, 5, 2, 5, 2, 5, 5, 6, 12, 4])
b_ub = np.array([-1, -1, 0, 0, 0])

bounds = []
for i in range(len(c)):
    bounds.append((0, None))

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(result)

