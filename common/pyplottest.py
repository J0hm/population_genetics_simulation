import matplotlib.pyplot as plt
import numpy as np
import tkinter as tkinter
import pylab
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure




graph = plt.figure()
graph, ax_lst = plt.subplots(1, 1)

array = np.array([[.5, .7, .9], [.4, .5, .6], [.8, .9, 1.0]])


# Implement this in genetics.py
def addNPGen(array, gen, avgFit, minFit, maxFit):
    return np.append(array, [[gen], [avgFit], [minFit], [maxFit]], axis=1)


root = tkinter.Tk()

fig = Figure(figsize=(5, 4), dpi=100)
t = array
axes = fig.add_subplot(111)
axes.plot(t)
axes.set_ylim([0,1])

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()


