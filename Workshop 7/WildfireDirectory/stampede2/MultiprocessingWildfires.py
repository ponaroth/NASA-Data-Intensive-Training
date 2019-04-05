import multiprocessing
import time

import matplotlib.pyplot as plt
import numpy as np

g = 0.0001


# ---------------------------------------------------------------

def make_random_forest(L, p):
    # first generate random array containing 1's with probability p
    forest = 1 * (np.random.random((L, L)) < p)
    # now set all the boundary elements to be 0
    forest[0, :] = 0
    forest[-1, :] = 0
    forest[:, 0] = 0
    forest[:, -1] = 0
    return forest


# ---------------------------------------------------------------

def plot_forest(forest):
    plt.figure(figsize=(6, 6))
    plt.pcolor(forest, vmin=0, vmax=2)


# forest = make_random_forest(10, 0.2)
# plot_forest(forest)

# ---------------------------------------------------------------
def to_burn_next_step_array(forest):
    # identify everywhere the forest is burning
    b = np.where(forest == 2, 1, 0)
    # count the number of burning neighbors at each site
    nb = np.roll(b, 1, axis=0) + np.roll(b, -1, axis=0) + np.roll(b, 1, axis=1) + np.roll(b, -1, axis=1)
    # return an array with 1 everywhere the forest has a tree and at least 1 neighbor is burning
    return np.where((forest == 1) * (nb > 0), 1, 0)


# ---------------------------------------------------------------

def update_empty(forest, updated):
    updated = np.where((forest == 0) * (np.random.random(forest.shape) < g), 1, updated)
    return updated


def update_trees(forest, updated):
    to_burn = to_burn_next_step_array(forest)
    updated = np.where(to_burn, 2, updated)
    return updated


def update_burning(forest, updated):
    updated = np.where((forest == 2), 0, updated)
    return updated


def enforce_boundary_conditions(updated):
    updated[0, :] = 0
    updated[:, 0] = 0
    updated[-1, :] = 0
    updated[:, -1] = 0
    return updated


# ---------------------------------------------------------------


def step(forest):
    updated = forest.copy()
    # empty (0) -> tree (1)
    updated = update_empty(forest, updated)
    # tree (1) -> burning (2)
    updated = update_trees(forest, updated)
    # tree (2) -> empty (0)
    updated = update_burning(forest, updated)
    # boundary conditions: 0 along boundary
    updated = enforce_boundary_conditions(updated)
    return updated


# ---------------------------------------------------------------

def lightning_strike(forest):
    random_tree_site = tuple([np.random.choice(idx) for idx in np.where(forest == 1)])
    forest[random_tree_site] = 2
    return forest


def simulate_one_fire(forest):
    num_trees = np.count_nonzero(forest == 1)
    if num_trees == 0:
        print("No trees left to burn")
        return forest, 0, 0

    forest = lightning_strike(forest)
    num_burning = np.count_nonzero(forest == 2)
    total_burned = num_burning
    duration = 0
    while (num_burning > 0):
        forest = step(forest)
        num_burning = np.count_nonzero(forest == 2)
        total_burned += num_burning
        duration += 1
    return forest, total_burned, duration


# ---------------------------------------------------------------

def simulate_many_fires(forest, Nfires):
    sizes = []
    durations = []

    for n in range(Nfires):
        forest, total_burned, duration = simulate_one_fire(forest)
        # if total_burned == 0:
        #    break
        sizes.append(total_burned)
        durations.append(duration)
    return forest, sizes, durations


# ---------------------------------------------------------------


def simulate_and_plot_many_fires(forest, Nfires):
    plt.figure(figsize=(8, 8))
    forest_start = forest.copy()
    for n in range(Nfires):
        forest, total_burned, duration = simulate_one_fire(forest)
        if total_burned == 0:
            break
    diff = forest - forest_start
    plt.pcolor(diff)
    return forest


# ---------------------------------------------------------------
def get_stats(L, p, Nfires, Ntrans):
    f = make_random_forest(L, p)
    f, sizes, durations = simulate_many_fires(f, Ntrans)
    f, sizes, durations = simulate_many_fires(f, Nfires)
    return f, sizes, durations


def get_multi_stats(L, p, Nprocesses, Nfires, Ntrans, Nmodels, filename=None):
    pool = multiprocessing.Pool(processes=Nprocesses)
    t1 = time.time()
    n_fillup = [(L, p, Nfires, Ntrans)] * Nmodels
    res = pool.starmap(get_stats, n_fillup)
    pool.close()
    pool.join()

    t2 = time.time()
    print("Processes: {}\tTime: {}".format(Nprocesses, t2 - t1))
    allsizes = []
    alldurations = []
    for elem in res:
        allsizes.extend(elem[1])
        alldurations.extend(elem[2])
    ST = np.stack((allsizes, alldurations), axis=1)
    if filename is not None:
        np.savetxt(filename, ST)
    return ST


def test_timing():
    max_cores = multiprocessing.cpu_count()

    # Working on skx-dev nodes
    if max_cores == 96:
        test_cores = [96, 72, 48, 24, 12, 6, 1]
        for n_cores in test_cores:
            _ = get_multi_stats(200, 0.4, n_cores, 100, 0, max_cores)
    # Working on development (KNL) nodes
    elif max_cores == 272:
        test_cores = [272, 136, 68, 34, 17, 1]
        for n_cores in test_cores:
            _ = get_multi_stats(200, 0.4, n_cores, 10, 0, max_cores)
    else:
        raise ValueError("Current Stampede2 queue not supported")


if __name__ == "__main__":
    test_timing()
