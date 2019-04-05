#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:06:25 2019

@author: slantz
"""
import matplotlib.pyplot as plt
import numpy as np
import random


def make_list_of_random_coords(n):
    L = []
    for i in range(n):
        L.append((2 * random.random() - 1, 2 * random.random() - 1))
    return L


def unit_circle_check(L):
    U = []
    for P in L:
        U.append(((P[0] * P[0] + P[1] * P[1]) ** 0.5) < 1)
    return U


if __name__ == '__main__':
    darts = make_list_of_random_coords(10000)
    hits = unit_circle_check(darts)
    pi_approx = 4 * hits.count(True) / len(hits)
    print("pi_approx = ", pi_approx)

    d_arr = np.array(darts)
    h_arr = np.array(hits)
    x = d_arr[:, 0]
    y = d_arr[:, 1]

    plt.rcParams['figure.figsize'] = (6, 6)
    plt.scatter(x[np.where(h_arr)], y[np.where(h_arr)], s=1, c='r', marker='.')
    plt.scatter(x[np.where(~h_arr)], y[np.where(~h_arr)], s=1, c='b', marker='.')
