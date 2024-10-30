# Author: Gavin Cramer / gmc0069@auburn.edu
# Date: 2024-10-29
# Assignment Name: hw04


import numpy as np

def p1(data, eval_pts):
    """
    Implement the divided difference method to interpolate the data points, 
    then evaluate the polynomial at the given point.

    @param data: a list of tuples [(x0, y0), (x1, y1), ..., (xn, yn)]
    @param eval_pts: a list of x values to evaluate the interpolating polynomial

    @return: a list of y values evaluated at the eval_pts

    """
    y = np.zeros(len(eval_pts))

    differs = []
    for x in range(len(data)+1):
        differs.append([])
    
    
    for row in range(len(differs)):
        for column in range(len(differs)):
            differs[row].append(None)
            
    coeff = []
    for c in range(len(data)):
        val, differs = helper(data, differs, 0, c)
        coeff.append(val)
    
    for evals in range(len(y)):
        result = coeff[0]
        for n in range(1, len(coeff)):
            value = coeff[n]
            for point in range(n):
                value*=(eval_pts[evals] - data[point][0])
            result += value
        
        y[evals] = result
        
    return y

def helper(data, matrix, lower, upper):
    if lower == upper: return data[lower][1], matrix
    if matrix[lower][upper]: return matrix[lower][upper], matrix
    matrix[lower][upper] = (helper(data, matrix, lower+1, upper)[0] - helper(data, matrix, lower, upper-1)[0])/(data[upper][0] - data[lower][0])
    return matrix[lower][upper], matrix


def p2(data, eval_pts):
    """
    For 6630 ONLY

    Implement the divided difference method to interpolate the data points, 
    then evaluate the polynomial at the given point.

    @param data: a list of tuples [(x0, y0, y0_1, y0_2, ..., y0_m1), 
                                   (x1, y1, y1_1, y1_2, ..., y1_m2),
                                    ..., 
                                   (xn, yn, yn_1, yn_2, ..., yn_mn)] 

                where x0, x1, ..., xn are the x values and the subsequent 
                values in the tuple are the derivatives of the function at the x values. 

                For example, 

                y0 = f(x0),
                y0_1 = f'(x0),
                y0_2 = f''(x0),
                ... ,
                y0_m1 = f^(m1)(x0)

    @param eval_pts: a list of x values to evaluate the interpolating polynomial

    @return: a list of y values evaluated at the eval_pts
    """
    y = np.zeros(len(eval_pts))

    # Write your code here.

    return y