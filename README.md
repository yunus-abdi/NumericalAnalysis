# NumericalAnalysis


1 Bisection Method

Suppose we want to find a root of the function f (x) on the interval [a, b] using
the bisection method. Here is the algorithm:

1. Let c = a+b
2 be the midpoint of the interval.
2. Evaluate f (c).
3. If f (c) = 0, then c is the root and we are done.
4. If f (c) has the same sign as f (a), then the root is in the interval [c, b]. Set
a = c and go to step 1.
5. If f (c) has the same sign as f (b), then the root is in the interval [a, c]. Set
b = c and go to step 1.

The bisection method is guaranteed to converge to a root of f (x) provided
that f (x) is continuous on [a, b] and f (a) and f (b) have opposite signs.


2 Newton-Raphson Method

Suppose we want to find a root of the function f (x) using the Newton-Raphson
method. Here is the algorithm:

1. Choose an initial guess x0.
2. Calculate f (x0) and f ′(x0).
3. Let x1 = x0 − f (x0)
f ′ (x0) .
4. Calculate f (x1) and f ′(x1).
5. Let x2 = x1 − f (x1)
f ′ (x1) .
6. Continue this process until the desired level of accuracy is achieved.

The Newton-Raphson method is guaranteed to converge to a root of f (x)
provided that f (x) is continuous and differentiable, and the initial guess is
sufficiently close to the root.
1
