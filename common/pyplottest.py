import matplotlib.pyplot as plt
import numpy as np
import tkinter as tkinter
import pylab
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure






array = np.array([[.5], [.4], [.8]])

# Implement this in genetics.py
def addNPGen(array, avgFit, minFit, maxFit):
    return np.append(array, [[avgFit], [minFit], [maxFit]], axis=1)

def replot(fig, array):
    axes.clear()
    axes.plot(array.T)
    axes.set_ylim(0, 1)

graph = plt.figure()
graph, ax_lst = plt.subplots(1, 1)
fig = Figure(figsize=(5, 4), dpi=100)
axes = fig.add_subplot(111)

print(array)

root = tkinter.Tk()6

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

replot(axes, array)



array = addNPGen(array, .6, .7, .8)
replot(axes, array)




tkinter.mainloop()


