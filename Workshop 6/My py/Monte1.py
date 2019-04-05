
import random
import matplotlib.pyplot as plt
import numpy as np
import math

print("throw darts")

# Assignment 1
# list1 = []
# for i in range(10000):
#     list1.append((random.random(), random.random()))
#
# print(list1[-1])




# Assignment #3 & 4
def make_list_of_random_coords(rang):
    list1 = []
    if (rang > 0):
        for i in range(rang):
            list1.append((random.random(), random.random()))

    return list1

# assignment 5
def unit_circle_check(list):
    u = []

    # for i in list:
        # distance between
        # dist_pow2 = math.pow(list[i][0], 2) - math.pow(list[i][1], 2)

        # dist = math.sqrt(dist_pow2)

        # print(list[i])

########## main ########


#Assignment #3, 4
list1 = make_list_of_random_coords(100)

print(type(list1), len(list1))

if __name__ == '__main__':
    darts = make_list_of_random_coords(10000)
    print(type(darts), len(darts))
    print(darts[0])


# 5
unit_circle_check(list1)