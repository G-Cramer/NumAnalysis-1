# Author: Gavin Cramer / gmc0069@auburn.edu
# Date: 2024-11-29
# Assignment Name: hw06

import numpy as np
import matplotlib.pyplot as plt

# Problem 1
def p1(func, a, b, n, option):
    """
    Implement composite quadrature rules for numerical integration
    of a function over the interval [a, b] with n subintervals.
    The option parameter determines the type of quadrature rule to use: 
    
    1 for the midpoint rule, 2 for the trapezoidal rule, and 3 for Simpson's rule.

    @param func: The function to integrate, provided as a function handle.
    @param a: The lower bound of the integration interval.
    @param b: The upper bound of the integration interval.
    @param n: The number of subintervals to use for the integration.
    @param option: The type of quadrature rule to use (1, 2, or 3).
    
    @return: The approximate integral of the function over the interval [a, b].
    """
    h = (b-a)/n
    terms = [a+k*h for k in range(n+1)]
    if option == 1:                 
        ret = h*sum(func((terms[j]+terms[j+1])/2) for j in range(n))
    elif option == 2:
        ret = (h/2)*(func(a) + func(b)) + h*sum(func(terms[j]) for j in range(1,n))
    elif option == 3:
        if n % 2 != 0:
            raise ValueError("The number of subintervals must be even for Simpson's rule.")
        ret = (h/3)*(func(a) + func(b) + 4*sum(func(terms[j]) for j in range(1, n, 2)) + 2*sum(func(terms[m]) for m in range(2, n-1, 2)))
    else:
        raise ValueError("Invalid option value. Must be 1, 2, or 3.")
    
    return ret


# Problem 2
def p2():
    """
    run with the following command: hw06.p2(). Do not edit this function.
    
    It checks the convergence of the composite quadrature rules implemented in p1.
    
    Here we use some examples, 
    f_1(x) = exp(x), 
    f_2(x) = (1 - x^2)^3, this function's first 2 derivatives at the endpoints are zero.
    f_3(x) = (1 - x^2)^5, this function's first 4 derivatives at the endpoints are zero.
    f_4(x) = (1 - x^2)^7, this function's first 6 derivatives at the endpoints are zero.

    Run this function will plot the figures for the convergence of the composite quadrature rules.
    Make comments about the results obtained from the plots. 
    
    > For instance, you can comment on the convergence rates of the quadrature rules, and how they compare to the theoretical rates.
    > Here are a few example questions you can answer in your comments:
    > Does the Runge phenomenon of f1 (Runge's function) lower the convergence rate?
    > Does Simpson's rule have a faster convergence rate than the other two for these examples?
    > Based on your observations, what kind of functions can have a faster convergence rate with the given composite quadrature rules?

    Write your comments here.
    >Simpson's rule has a higher error than midpoint and trapezoidal rules for all of the polynomial functions
    >Simpson's rule does much better for e^x than the other two rules
    >Trapezoidal and midpoint rules are noticably similar to eachother in each example
    >convergence rates always increase/errors always decrease w/ more subintervals
    >for the polynomials, the higheer exponents of the (1-x^2) term lead to lower errors for given subinterval amounts
    >simpson's rule errors for exp(x) and (1-x^2)^3 are noticably similar, whereas they are much better for the polynomials for the other 2 rules
    >               
    """
    funcs = [np.exp,
             lambda x: (1 - x**2)**3,
             lambda x: (1 - x**2)**5,
             lambda x: (1 - x**2)**7]

    funcs_names = ['exp(x)', '(1 - x^2)^3', '(1 - x^2)^5', '(1 - x^2)^7']

    exact = [np.exp(1) - np.exp(-1), 32/35, 512/693, 4096/6435]

    n = 2**np.arange(1, 9)

    for k, func in enumerate(funcs):
        errors = np.zeros((3, len(n)))
        for i, n_i in enumerate(n):
            for j in range(3):
                errors[j, i] = np.abs(p1(func, -1, 1, n_i, j+1) - exact[k])

        plt.figure(k)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.plot(n, errors[0, :], 'r-', label='Midpoint Rule')
        plt.plot(n, errors[1, :], 'g-', label='Trapezoidal Rule')
        plt.plot(n, errors[2, :], 'b-', label="Simpson's Rule")
        plt.plot(n, 1/n**2, 'm--', label='2nd order convergence')
        plt.plot(n, 1/n**4, 'k-.', label='4nd order convergence')
        plt.plot(n, 1/n**6, 'm--d', label='6nd order convergence')
        plt.plot(n, 1/n**8, 'k--o', label='8nd order convergence')
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('number of subintervals')
        plt.ylabel('Error')
        plt.title(f'Convergence of Quadrature Rules for {funcs_names[k]}')
        plt.legend()
    plt.show()



# Problem 3
def p3(func, a, b, N, option):
    """
    Use your implemented Richardson extrapolation function in HW05 to implement the Romberg integration method.
    
    @param func: The function to integrate, provided as a function handle.
    @param a: The lower bound of the integration interval.
    @param b: The upper bound of the integration interval.
    @param N: it means 2^N is the maximum number of subintervals to use for the integration. 
              The Romberg method will start with 2^1=2 subintervals and double the number of subintervals until 2^N
    @param option: The type of quadrature rule to use (1, 2, or 3). See p1.
    
    @return: The approximate integral of the function over the interval [a, b].

    Note, the "powers" used in Richardson extrapolation (see hw05.m) should be [2, 4, 6, ...] for option 1 and 2. 
    For option 3, the "powers" should be [4, 6, 8, ...].
    """
    table = np.zeros((N, N))
    start = 0
    #if option == 3: start+=1
    for i in range(start, N):
        table[i][0] = p1(func, a, b, 2**(i+1), option)
    
    for j in range(1, N):
        for k in range(j+start, N):
            table[k][j] = ((4**j)*table[k][j-1] - table[k-1][j-1])/(4**j - 1)

    return table[-1][-1-start]

# Problem 4
def p4():
    """
    Construct the Gauss quadrature rule using the roots of the Legendre polynomial of degree 6.
     
    To evaluate Legendre polynomial of degree 6, use the helper function legendre_poly_6 defined below.

    @return: A 6x2 numpy matrix containing the roots and weights of the Gauss quadrature rule. 
             The first column contains the roots and the second column contains the corresponding weights.
    """

    roots = np.zeros(6)
    weights = np.zeros(6)
    
    eps = 10**(-14)
    brackets = [-1, -3/4, -1/4, 0, 1/4, 3/4, 1]
    for b in range(len(brackets)-1):
        roots[b] = bisection(brackets[b], brackets[b+1], eps)
        weights[b] = 2/((1 - roots[b]**2)*(l_prime(roots[b]))**2)
    
    ret = np.column_stack((roots, weights))

    return ret

def bisection(a, b, epsilon):
    c = (a+b)/2
    while abs(legendre_poly_6(c)) > epsilon:
        if legendre_poly_6(a)*legendre_poly_6(c)<0:
            b = c
        else:
            a = c
        c = (a+b)/2
    return c

def l_prime(x):
    return (231*6*x**5 - 315*4*x**3 + 105*2*x)/16
    
# Problem 5
def p5(n):
    """
    For 6630 ONLY. 

    Construct the Gauss quadrature rule using the roots of the Legendre polynomial of degree n
    
    @param n: The degree of the Legendre polynomial for the nodes of the Gauss quadrature rule.
    @return: An nx2 numpy matrix containing the roots and weights of the Gauss quadrature rule.
    
    To evaluate Legendre polynomial or its derivative of a specific degree n, use the following two functions.
                  
    legendre_poly_n = lambda x: legendre_poly(n, x)
    deriv_legendre_poly_n = lambda x: deriv_legendre_poly(n, x)
    
    """
    roots = np.zeros(n)
    weights = np.zeros(n)

    # your code here.


    ret = np.column_stack((roots, weights))
    return ret

###############################################################################
#                                                                             #
# Helper functions for Problem 4 and 5, do not modify these functions         #
#                                                                             #
###############################################################################

# Helper function for p4
def legendre_poly_6(x):
    """
    Evaluate the Legendre polynomial of degree 6 at x.
    
    @param x: The value at which to evaluate the Legendre polynomial.
    @return: The value of the Legendre polynomial of degree 6 at x.
    """
    return (231*x**6 - 315*x**4 + 105*x**2 - 5)/16

# Helper functions for p5
def legendre_poly(n, x):
    """
    Evaluate the Legendre polynomial of degree n at x.
    
    @param n: The degree of the Legendre polynomial to evaluate.
    @param x: The value at which to evaluate the Legendre polynomial.
    @return: The value of the Legendre polynomial of degree n at x.
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return (2*n - 1)/n*x*legendre_poly(n-1, x) - (n - 1)/n*legendre_poly(n-2, x)

# Helper functions for p5
def deriv_legendre_poly(n, x):
    """
    Evaluate the derivative of the Legendre polynomial of degree n at x.
    
    @param n: The degree of the Legendre polynomial whose derivative to evaluate.
    @param x: The value at which to evaluate the derivative of the Legendre polynomial.
    @return: The value of the derivative of the Legendre polynomial of degree n at x.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n/(x**2 - 1)*(x*legendre_poly(n, x) - legendre_poly(n-1, x))