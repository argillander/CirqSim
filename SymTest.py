from sympy import *
import numpy as np

res = np.matmul([[1,0]], [[1, 1],[1, -1]])
norm = np.linalg.norm(res)
res = np.multiply(res, norm)

m = Matrix([[1,1], [1, -1]])
v = Matrix([[1,0]])
res2 = v* (m)
pprint(m)
print()
pprint(v)
res2 = res2 * (1/res2.norm())


print()
pprint(res2)
