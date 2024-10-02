# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:11:30 2024

@author: gavin
"""

# Author: Your Name / your_email
# Date: 2024-09-01
# Assignment Name: hw02

import sys
import numpy as np

def p1(f, a, b, epsilon, name, f_prime=None):
    """
    @param f: a function name
    @param a: real number, the left end of the interval
    @param b: real number, the right end of the interval
    @param epsilon: function tolerance
    @param name: the name of the method to use
    @param f_prime: the derivative of the function f (only needed for Newton's method)

    @return: tuple (c, n), 
             c is the root of the function f in the interval [a, b]
             n is the number of iterations
    """
    # Write your code here (bisection code is provided)
    if name=="bisection":
        # bisection method
        n = 0
        c = (a+b)/2
        while abs(f(c))>epsilon:
            n += 1
            if f(a)*f(c)<0:
                b = c
            else:
                a = c
            c = (a+b)/2
        return c,n
    elif name=="newton":
        n = 0
        c = a
        while abs(f(c))>epsilon:
            n+=1
            c = c - f(c)/f_prime(c)
        return c,n
    elif name=="secant":
       n = 0
       c = b
       while abs(f(c))>epsilon:
           n+=1
           c = b - f(b)*(b-a)/(f(b) - f(a))
           a = b
           b = c
       return c,n
    elif name=="regula_falsi":
        n=0
        c = a - f(a)*(b - a)/(f(b) - f(a))
        while abs(f(c))>epsilon:
            n+=1
            a = c
            c = a - f(a)*(b - a)/(f(b) - f(a))
        return c,n
    elif name=="steffensen":
        n = 0
        c = a
        while abs(f(c)) > epsilon:
            g = (f(c + f(c)) - f(c))/f(c)
            c = c - f(c)/g
        return c,n
    else:
        print("Invalid name")
        
def p2():
    """
    summarize the iteration number for each method name in the table

    |name          | iter | 
    |--------------|------|
    |bisection     |4      |
    |secant        |4      |
    |newton        |4      |
    |regula_falsi  |4      |
    |steffensen    |4      |
    """


def p3(f, a, b , epsilon):
    """
    For 6630 students only.

    Implement the Illinois algorithm to find the root of the function f in the interval [a, b]

    @param f: a function name
    @param a: real number, the left end of the interval
    @param b: real number, the right end of the interval
    @param epsilon: function tolerance

    @return: tuple (c, n), 
             c is the root of the function f in the interval [a, b]
             n is the number of iterations
    """
    # Write your code here
    pass

def p4(f, a, b , epsilon):
    """
    For 6630 students only.

    Implement the Pegasus algorithm to find the root of the function f in the interval [a, b]

    @param f: a function name
    @param a: real number, the left end of the interval
    @param b: real number, the right end of the interval
    @param epsilon: function tolerance
    
    @return: tuple (c, n), 
             c is the root of the function f in the interval [a, b]
             n is the number of iterations
    """
    # Write your code here
    pass