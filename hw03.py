# Author: Gavin Cramer / gmc0069@auburn.edu
# Date: 2024-09-01
# Assignment Name: hw03

import numpy as np

def p1(data, eval_pts):
    """
    Implement the Lagrange interpolation method, and evaluate the interpolating polynomial 
    at the given points.

    @param data: a list of tuples [(x0, y0), (x1, y1), ..., (xn, yn)]
    @param eval_pts: a list of x values to evaluate the interpolating polynomial

    @return: a list of y values evaluated at the eval_pts
    """
    y = np.zeros(len(eval_pts))

    for i in range(len(eval_pts)):
        q = 1
        
        for counter in range(len(data)):
            q = q*(eval_pts[i] - data[counter][0])
        
        lagrange = 0
        for j in range(len(data)):
            k_j = 1
        
            for k in range(len(data)):
                if k == j: continue
                k_j = k_j*(data[j][0] - data[k][0])  
            
            k_j = k_j**(-1)
            lagrange += data[j][1]*k_j/(eval_pts[i] - data[j][0])
        lagrange = lagrange*q
        y[i] = lagrange

    return y



def p2():
    """
    Use equally spaced nodes and Chebyshev nodes to compute the Lagrange polynomial interpolation of 
    f(x) = 1/(1 + 25x^2) and g(x) = sin(pi * x) on [-1, 1]. 
    This code uses your implementation of p1 to compute the
    interpolation, and record the maximum interpolation error at 1000 equally 
    spaced points in [-1, 1].
    ----------------------------------------------------------------------------------

    First, run this function and tabulate your result in the table below. 
    Then, make a comment/explanation on the trend of the error for **equally spaced nodes** 
    as n increases for each function.

    Write your comments here:
    >I consistently got underflow for the error,although this may be due to the precision level of my system.
    >
    >
    >
    >
    
    
    |n  |                        Function       | Error with equally spaced nodes | Error with Chebyshev nodes  |
    |---|---------------------------------------|---------------------------------|-----------------------------|    
    | 5 | 1 / (1 + 25 * x ** 2)                 |              nan                |       5.5589e-01            |
    |10 | 1 / (1 + 25 * x ** 2)                 |              nan                |       1.0915e-01            |
    |15 | 1 / (1 + 25 * x ** 2)                 |              nan                |       8.3094e-02            |
    |20 | 1 / (1 + 25 * x ** 2)                 |              nan                |       1.5333e-02            |
    |25 | 1 / (1 + 25 * x ** 2)                 |              nan                |       1.1411e-02            |
    |30 | 1 / (1 + 25 * x ** 2)                 |              nan                |       2.0613e-03            |
    |35 | 1 / (1 + 25 * x ** 2)                 |              nan                |       1.5642e-03            |
    |40 | 1 / (1 + 25 * x ** 2)                 |              nan                |       2.8935e-04            |
    |45 | 1 / (1 + 25 * x ** 2)                 |              nan                |       2.1440e-04            |
    |50 | 1 / (1 + 25 * x ** 2)                 |              nan                |       3.9629e-05            |
    |55 | 1 / (1 + 25 * x ** 2)                 |              nan                |       2.9383e-05            |
    |---|---------------------------------------|---------------------------------|-----------------------------|
    | 5 | np.sin(np.pi * x)                     |              nan                |       1.3193e-02            |
    |10 | np.sin(np.pi * x)                     |              nan                |       6.0348e-06            |
    |15 | np.sin(np.pi * x)                     |              nan                |       2.0995e-11            |
    |20 | np.sin(np.pi * x)                     |              nan                |       1.4433e-15            |
    |25 | np.sin(np.pi * x)                     |              nan                |       1.5543e-15            |
    |30 | np.sin(np.pi * x)                     |              nan                |       1.4433e-15            |
    |35 | np.sin(np.pi * x)                     |              nan                |       1.3323e-15            |
    |40 | np.sin(np.pi * x)                     |              nan                |       2.1094e-15            |
    |45 | np.sin(np.pi * x)                     |              nan                |       1.7764e-15            |
    |50 | np.sin(np.pi * x)                     |              nan                |       1.9984e-15            |
    |55 | np.sin(np.pi * x)                     |              nan                |       2.5535e-15            |
    |---|---------------------------------------|---------------------------------|-----------------------------|
    
    """
    eval_pts = np.linspace(-1, 1, 1000)
    f = lambda x: 1 / (1 + 25 * x ** 2)
    f.__name__ = '1 / (1 + 25 * x ** 2)'
    g = lambda x: np.sin(np.pi * x)
    g.__name__ = 'np.sin(np.pi * x)'
    funcs = [f, g]

    print('|n  |                        Function       | Error with equally spaced nodes | Error with Chebyshev nodes  |');
    print('|---|---------------------------------------|---------------------------------|-----------------------------|');

    for i in range(2):
        for n in range(5, 60, 5):
            eq_data = [(x, funcs[i](x)) for x in np.linspace(-1, 1, n+1)]
            y = p1(eq_data, eval_pts)
            eq_error = np.max(np.abs(funcs[i](eval_pts) - y))

            cheb_data = [(np.cos((2 * k + 1) * np.pi / (2 * n + 2)), funcs[i](np.cos((2 * k + 1) * np.pi / (2 * n + 2)))) for k in range(n+1)]
            y = p1(cheb_data, eval_pts)
            cheb_error = np.max(np.abs(funcs[i](eval_pts) - y))

            print(f'|{n:2d} | {funcs[i].__name__:30s}        | {eq_error:16.4e}                | {cheb_error: 16.4e}            |')
        print('|---|---------------------------------------|---------------------------------|-----------------------------|');


def p3():
    """
    For 6630 students only.

    Use the extreme Chebyshev nodes to compute the Lagrange polynomial interpolation of 
    f(x) = 1/(1 + 25x^2) and g(x) = sin(pi * x) on [-1, 1]. 
    This code uses your implementation of p1 to compute the
    interpolation, and record the maximum interpolation error at 1000 equally spaced points in [-1, 1].
    ----------------------------------------------------------------------------------

    Run this function and tabulate your result in the table below. 
    Then, make a comment on the performance of the extreme Chebyshev nodes compared to Chebyshev nodes.

    Write your comments here.
    >
    >
    >
    >
    >

    
    |n  |                        Function       | Error with extreme Chebyshev nodes  |
    |---|---------------------------------------|-------------------------------------|
    | 5 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |10 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |15 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |20 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |25 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |30 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |35 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |40 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |45 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |50 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |55 | 1 / (1 + 25 * x ** 2)                 |                                     |
    |---|---------------------------------------|-------------------------------------|
    | 5 | np.sin(np.pi * x)                     |                                     |
    |10 | np.sin(np.pi * x)                     |                                     |
    |15 | np.sin(np.pi * x)                     |                                     |
    |20 | np.sin(np.pi * x)                     |                                     |
    |25 | np.sin(np.pi * x)                     |                                     |
    |30 | np.sin(np.pi * x)                     |                                     |
    |35 | np.sin(np.pi * x)                     |                                     |
    |40 | np.sin(np.pi * x)                     |                                     |
    |45 | np.sin(np.pi * x)                     |                                     |
    |50 | np.sin(np.pi * x)                     |                                     |
    |55 | np.sin(np.pi * x)                     |                                     |
    |---|---------------------------------------|-------------------------------------|
    
    
    """
    eval_pts = np.linspace(-1, 1, 1000)
    f = lambda x: 1 / (1 + 25 * x ** 2)
    f.__name__ = '1 / (1 + 25 * x ** 2)'
    g = lambda x: np.sin(np.pi * x)
    g.__name__ = 'np.sin(np.pi * x)'
    funcs = [f, g]
    print('|n  |                        Function       | Error with extreme Chebyshev nodes  |');
    print('|---|---------------------------------------|-------------------------------------|');
    for i in range(2):
        for n in range(5, 60, 5):
            ex_cheb_data = [(np.cos((k) * np.pi / (n)), funcs[i](np.cos(k * np.pi / (n)))) for k in range(n+1)]
            y = p1(ex_cheb_data, eval_pts)
            cheb_error = np.max(np.abs(funcs[i](eval_pts) - y))
            print(f'|{n:2d} | {funcs[i].__name__:30s}        | {cheb_error: 16.4e}                    |')
        print('|---|---------------------------------------|-------------------------------------|');