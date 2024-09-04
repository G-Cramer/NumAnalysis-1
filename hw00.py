# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:36:57 2024

@author: gavin
"""

# Author: Gavin Cramer / gmc0069@auburn.edu
# Date: 2024-09-01
# Assignment Name: hw00

import numpy as np
import time 

# The following class defines 3 functions for each problem respectively.
# Please follow the instruction inside each function. 

def p1(m):
    """
    This function takes an integer m and returns the term a_m in the sequence defined by 
    a_0 = 0, a_1 = 1, a_2 = 1, and a_n = a_{n-1} + a_{n-2} + a_{n-3} for n >= 3.
    :param m: an integer
    :return: the m-th term in the sequence
    """
    if m < 0:
        return None
    
    if m == 0:
        return 0
    if m < 3:
        return 1
    
    return p1(m-1) + p1(m-2) + p1(m-3)
    

def p2(A):
    """
    This function takes a numpy matrix A of size n x n and returns the determinant of A.
    :param A: a numpy matrix of size n x n
    :return: the determinant of A
    """
    size = A.shape[0]
    
    if size != A.shape[1]:
        return None
    
    if size == 1:
        return A[0][0]
    
    if size == 2:
        return A[0][0]*A[1][1] - A[1][0]*A[0][1]
    
    
    first_col = np.array([A[x][0] for x in range(size)])
    toReturn = 0

    for index in range(size):
        new_array = np.copy(A) 
        new_array = np.delete(new_array, 0, axis = 1)
        new_array = np.delete(new_array, index, axis = 0)
        toReturn += ((-1)**(index))*first_col[index]*p2(new_array)
        
    return toReturn
    
    

    
        
        

def p3():
    """
    This function should have a run time about 1 second.
    :return: no returns
    """
    time.sleep(1)
    