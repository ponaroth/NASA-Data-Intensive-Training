#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:18:04 2019

@author: slantz
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import time
    
def make_list_of_random_coords(n):
    L = []
    for i in range(n):
        L.append((2*random.random()-1, 2*random.random()-1))
    return L

def unit_circle_check(L):
    U = []
    for P in L:
        U.append(((P[0]*P[0] + P[1]*P[1])**0.5)<1)
    return U

def throw_darts(n):
    darts = 2*np.random.random((n,2)) - 1
    return darts

def in_unit_circle(p):
    return np.linalg.norm(p,axis=1)<1

if __name__ == '__main__':
    n = 1000000
    print("n =", n)

    start = time.time()
    darts = make_list_of_random_coords(n)
    hits = unit_circle_check(darts)
    pi_approx1 = 4 * hits.count(True) / len(hits)
    t1 = time.time() - start
    formstr = "pi_approx1 = {:2.10f}, t1 = {:2.4f}"
    print(formstr.format(pi_approx1,t1))
    
    start = time.time()
    d_arr = throw_darts(n)
    h_arr = in_unit_circle(d_arr)
    pi_approx2 = 4 * np.sum(h_arr) / n
    t2 = time.time() - start
    formstr = "pi_approx2 = {:2.10f}, t2 = {:2.4f}"
    print(formstr.format(pi_approx2,t2))
    