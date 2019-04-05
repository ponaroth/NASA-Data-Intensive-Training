import random as rand
import matplotlib.pyplot as plt
import numpy as np


# return a list of random coordinates
def generate_sample(n):
    sample = []
    for i in range(n):
        sample.append((rand.random(), rand.random()));
    return sample


# check each coordinate if they are inside the circle and return a list of booleans
def unit_circle_check(sample):
    L = []
    for c in sample:
        L.append(((c[0] * c[0] + c[1] * c[1]) ** 0.5) < 1)
    return L


if __name__ == '__main__':
    # generate a list 10,000 coordinates
    sample1 = generate_sample(100000)
    print(type(sample1), len(sample1))

    # check the coordinates to see if they are in the circle
    hits = unit_circle_check(sample1)

    # calculate PI
    pi = 4 * hits.count(True) / len(hits)
    print("experimental PI = ", pi)

    # Use matplotlib to visualize the data
    d_arr = np.array(sample1)
    x = d_arr[:, 0]
    y = d_arr[:, 1]
    h_arr = np.array(hits)

    plt.rcParams['figure.figsize'] = (8, 8)
    plt.scatter(x[np.where(h_arr)], y[np.where(h_arr)], s=1, c='r', marker='.')
    plt.scatter(x[np.where(~h_arr)], y[np.where(~h_arr)], s=1, c='b', marker='.')