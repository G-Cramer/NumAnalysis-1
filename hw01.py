# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:27:52 2024

@author: gavin
"""

# Author: Your Name / your_email
# Date: 2024-09-01
# Assignment Name: hw01

import sys
import numpy as np

def p1():
    """
    This function only contains comments. Fill the following table. Do not write any code here.

    commands                                      |  results            | explanations
    ----------------------------------------------|---------------------|----------------
    import sys;sys.float_info.epsilon             |2.220446049250313e-16|machine error
    import sys;sys.float_info.max                 |1.7976931348623157e+308|maximum bound of machine
    import sys;sys.float_info.min                 |2.2250738585072014e-308|minimum positive value of machine
    import sys;1 + sys.float_info.epsilon - 1     |2.220446049250313e-16|shows that the machine error still equals itself
    import sys;1 + sys.float_info.epsilon /2 - 1  |0.0                  |dividing epsilon by 2 puts it within margin for error, leading to value to be outputted as 0
    import sys;sys.float_info.min/1e10            |2.225074e-318        |rounding within floating point range
    import sys;sys.float_info.min/1e16            |0.0                  |rounding out of range, underflwows to 0
    import sys;sys.float_info.max*10              |inf                  |rounding ou tof range, overflows to infinity
    """

def p2(n, choice):
    """
    This function computes the Archimedes' method for pi.
    @param n: the number of sides of the polygon
    @param choice: 1 or 2, the formula to use
    @return: s_n, the approximation of pi using Archimedes' method.

    
    Tabulate the error of |s_n - pi| for n = 0, 1, 2, ... 15 and choices n = 1, 2
    for both choices of formulas.
    
    n     | choice 1 | choice 2
    ------|----------|----------
    0     |0.32250896154796127    |0.32250896154796127
    1     |0.0737976555836779     |0.07379765558367923
    2     |0.018067288507700674   |0.01806728850770778
    3     |0.00449356154160796    |0.004493561541642155
    4     |0.0011219460555205174  |0.0011219460555755845
    5     |0.00028039639033305974 |0.0002803963900310791
    6     |7.009346501529734e-05  |7.009346705633135e-05
    7     |1.752300998747458e-05  |1.7523014897768974e-05
    8     |4.380733284570226e-06  |4.380731734698884e-06
    9     |1.0952273221676023e-06 |1.0951815605508841e-06
    10    |2.742835807367783e-07  |2.7379530465054813e-07
    11    |7.20330572967498e-08   |6.844882172174493e-08
    12    |1.815149275330441e-08  |1.7112205874525444e-08
    13    |3.468864750999501e-08  |4.2780525788543855e-09
    14    |1.815149275330441e-08  |1.069514254936621e-09
    15    |7.177075609376971e-07  |2.673798960017848e-10
 

    Explanation of the results:
        the 2 choices' differences in their formulas lead to a slight difference in accuracy,
        which becomes relatively more pronounced as the formula is iterated and the error shrinks
        at differing rates

    """

    # Write your code here
    p_n = 3**(-1/2)
    if choice == 1:
        for x in range(n):
            p_n = (((1 + (p_n)**2)**(1/2))-1)/p_n
    
    else:
        for x in range(n):
            p_n = p_n/(1 + ((1 + (p_n)**2)**(1/2)))
                       
    s_n = p_n*6*(2**n)
    return s_n

def p3(a):
    """
    This function implements the Kahan summation algorithm. 

    @param a: a 1D numpy array of numbers
    @return: the Kahan sum of the array
    """
    j = 1
    e = 0
    s = a[0]
    size = a.size
    while j < size:
        y = a[j] - e
        old_s = s
        s = s + y
        e = (s - old_s) - y
        j+=1
    return s        
        
def p4(a):
    """
    This function tests the performance of Kahan summation algorithm 
    against naive summation algorithm.

    @param a: a 1D numpy array of numbers
    @return: no return

    @task: Test this function with a = np.random.rand(n) with various size n multiple times. Summarize your findings below.

    @findings:
        I tested p4 with random numpy arrays ranging from sizes 1 through 50. As expected,
        errors for the most part were relatively greater (from e-10 to e-7) as n increased.
        Something to note is that for every test of the function, the two errors were 
        always equal to one another.




    """
    single_a = a.astype(np.float32) # Convert the input array to single precision
    s = p3(a) # Kahan sum of double precision as the ground truth
    single_kahan_s = p3(single_a) # Kahan sum of single precision
    single_naive_s = sum(single_a) # Naive sum of single precision

    print(f"Error of Kahan sum under single precision: {s - single_kahan_s}")
    print(f"Error of Naive sum under single precision: {s - single_naive_s}")

def p5(a):
    """
    For 6630. 

    This function computes summation of a vector using pairwise summation.
    @param a: a vector of numbers
    @return: the summation of the vector a using pairwise summation algorithm.

    @note: You may need to create a helper function if your code uses recursion.

    @task: Rewrite the p4 test function to test this summation method. Summarize your findings below.
    
    @findings: 
    
    
    
    
    
    """

    return 0 # Write your code here.