#Newton Raphison method
import timeit
mysetups = "import math"

#codes to be executed
mycodes= """
def f(x):
    return (x**4-2*x**3-5*x-2)

a = 2
b = 3
max_iteration = 100
tolerance = 1e-6

def df(x):
    return (4*x**3-6*x**2-5)
x_initial = 2

for i in range(max_iteration):
    fx = f(x_initial)
    dfx = df(x_initial)
    x1 = x_initial -(fx/dfx)
    # print(f'n0 of iteration is {i}')
    if abs(f(x1)) < tolerance:
        print(f'root of x is {x1}')
        break
    else:
        x_initial = x1"""

print("time takes to run the program is: ", timeit.timeit(setup= mysetups,
    stmt = mycodes,
    number = 1))