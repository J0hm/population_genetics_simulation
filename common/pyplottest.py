import matplotlib.pyplot as plt
import numpy as np


graph = plt.figure()
graph, ax_lst = plt.subplots(1, 1)

array = np.array([[1, 2, 3], [.5, .7, .9], [.4, .5, .6], [.8, .9, 1.0]])

# Implement this in genetics.py
def addNPGen(array, gen, avgFit, minFit, maxFit):
    return np.append(array, [[gen], [avgFit], [minFit], [maxFit]], axis=1)


array = addNPGen(array, 4, .7, .6, .9)


print(array)

