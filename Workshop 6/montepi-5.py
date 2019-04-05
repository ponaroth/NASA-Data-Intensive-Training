#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:18:04 2019

@author: slantz
"""
import matplotlib.pyplot as plt
import numpy as np
import time
    
def throw_darts(n):
    darts = 2*np.random.random((n,2)) - 1
    return darts

def in_unit_circle(p):
    return np.linalg.norm(p,axis=1)<1

def estimate_pi(n):
    d_arr = throw_darts(n)
    h_arr = in_unit_circle(d_arr)
    return 4 * np.sum(h_arr) / n

if __name__ == '__main__':
    n_ests = 10000
    n = 10000
    N = n_ests*n
    
    start = time.time()
    pi_ests = []
    for i in range(n_ests):
        pi_ests.append(estimate_pi(n))
    t = time.time() - start
    print("N = {:d}, t = {:2.4f}".format(N, t))
   
    while n_ests >= 100:
        pi_est_mean = np.mean(pi_ests)
        pi_est_std  = np.std(pi_ests)
        formstr = "pi_est_mean = {:2.10f}, pi_est_std = {:2.10f}, n = {:d}"
        print(formstr.format(pi_est_mean, pi_est_std, n))
        plt.figure()
        plt.hist(pi_ests)
        pi_ests = np.reshape(pi_ests, (-1, 10))
        pi_ests = 0.1 * np.sum(pi_ests, axis=1)
        n = n * 10
        n_ests = n_ests / 10
        