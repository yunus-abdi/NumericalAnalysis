import timeit
 
 #codes snippet to be run once and before the actual code 
mysetups = "import math"



mycodes = """
def f(x):
    return (x**4-2*x**3-5*x-2)

a = 2
b = 3
max_iteration =  10**10
tolerance = 1e-6

for i in range(max_iteration):
    c = (a+b)/2
    if abs(f(c)) < tolerance :
        print(f'root found at x = {c: .6f}')
        break
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c
        """
print ("time is: ", timeit.timeit(setup=mysetups, 
                    stmt= mycodes,
                    number = 1))
