#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:13:26 2019

@author: slantz
"""
import matplotlib.pyplot as plt
import numpy as np
import random

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
    n = 10000
    
    darts = make_list_of_random_coords(n)
    hits = unit_circle_check(darts)
    pi_approx1 = 4 * hits.count(True) / len(hits)
    print("pi_approx1 = ", pi_approx1)
    
    d_arr = throw_darts(n)
    h_arr = in_unit_circle(d_arr)
    pi_approx2 = 4 * np.sum(h_arr) / n
    print("pi_approx2 = ", pi_approx2)
    
#    d_arr = np.array(darts)
#    h_arr = np.array(hits)
    x = d_arr[:,0]
    y = d_arr[:,1]
    
    plt.rcParams['figure.figsize'] = (6,6)
    plt.scatter(x[np.where(h_arr)], y[np.where(h_arr)], s=1, c='r', marker='.')
    plt.scatter(x[np.where(~h_arr)], y[np.where(~h_arr)], s=1, c='b', marker='.')
