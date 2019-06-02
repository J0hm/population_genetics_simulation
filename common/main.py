import random as rand
import time
from genetics import *
from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import time


# These are constants but cannot be delcared as such in python
# Changing them changes how the basic algorithms function
alleleCount = 32
popSize = 256
mutationChance = 0.05

# Declaring the globals
individualGenList = []
currentGen = 0
desiredChromosome = ""
lastGenPopList = []
npGenStats = [[0], [0], [0]]
peakFitness = 0



# The main window class
class Window(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)               
                self.master = master
                self.init_window()

        def init_window(self):
                self.master.title("Population Genetics Simulator")
                self.pack(fill=BOTH, expand=1)

# Class for storing data about whole generations
class individualGeneration():
        def __init__(self):
                self.maxFitness = 0
                self.minFitness = 0
                self.meanFitness = 0
                self.populationList = []


# Adds generation to numpy array : must be in order
def addNPGen(individualGenerationObject):
        global npGenStats
        npGenStats = np.append(npGenStats, [[individualGenerationObject.meanFitness], [individualGenerationObject.minFitness], [individualGenerationObject.maxFitness]], axis=1)


def replot():
        global npGenStats
        # Sets up graph and array
        plt.close('all')
        graph = plt.figure()
        graph, ax_lst = plt.subplots(1, 1)
        fig = Figure(figsize=(6, 8), dpi=100)
        figAxes = fig.add_subplot(111)
        figAxes.plot(npGenStats[0].T, '-g', label="Average")
        figAxes.plot(npGenStats[1].T, '-b', label="Min")
        figAxes.plot(npGenStats[2].T, '-r', label="Max")
        figAxes.legend(loc='upper left')
        figAxes.set_title("Fitness Over Generations")
        figAxes.set_ylabel("Fitness")
        figAxes.set_xlabel("Generation")
        figAxes.set_ylim(0, 1)
        # Places canvas to draw graph
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=700, y=-65)


# Places a label with text at x,y. Streamlines this process but is not ideal for every situation, as it does not let you change the value of the label
def placeLabelAtPos(window, labelText, xPos, yPos, fontType = "Helvectica", fontSize = 16):
        newPlacedLabel = Label(window, text = labelText, font=(fontType, fontSize))
        newPlacedLabel.place(x=xPos, y=yPos)


# Creates a new gen0 and genList
def newGenList(alleleCount, popSize):
        global lastGenPopList
        global desiredChromosome

        popList = createPopulation(popSize, alleleCount)
        desiredChromosome = randChromosome(alleleCount)

        calculateFitness(desiredChromosome, popList, alleleCount)

        findReproductionChance(popList)
        popList = sortByReprodutionChance(popList)

        popMeanFitness = meanFitness(popList)
        popMinFitness = minFitness(popList)
        popMaxFitness = maxFitness(popList)

        # Creates the main list for keeping data over generations
        individualGenList = []

        # Adds gen0 (starting gen) to 
        gen0 = individualGeneration()
        gen0.maxFitness = popMaxFitness
        gen0.minFitness = popMinFitness
        gen0.meanFitness= popMeanFitness
        gen0.populationList = popList

        lastGenPopList = popList

        individualGenList.insert(0, gen0)

        return individualGenList


# Restarts simulation
def restartSimulation():
        global currentGen
        global individualGenList
        global npGenStats
        global peakFitness

        individualGenList = newGenList(int(alleleCountEntry.get()), int(popSizeEntry.get()))
        currentGen = 0

        # Resets NP array to gen 0
        npGenStats = np.array([[individualGenList[0].meanFitness], [individualGenList[0].minFitness], [individualGenList[0].maxFitness]])
        replot()

        peakFitness = individualGenList[0].maxFitness
        fitnessPeakLabel.config(text=("Peak Fitness (all gens): " + str(round(peakFitness, 8))))

        genLabelText = "Current Generation: " + str(currentGen)
        labelGeneration.config(text=genLabelText)
        averageLabelText = "Average Fitness: " + str(round(individualGenList[0].meanFitness, 5))
        labelMeanFitness.config(text=averageLabelText)
        newMinFitnessText = "Min Fitness: " + str(round(individualGenList[0].minFitness, 5))  
        newMaxFitnessText = "Max Fitness: " + str(round(individualGenList[0].maxFitness, 5)) 
        labelMinFitness.config(text=newMinFitnessText)
        labelMaxFitness.config(text=newMaxFitnessText)

        genListBox.delete(0, END)
        newGen0Text = "Generation 0: " + str(individualGenList[0].meanFitness)
        genListBox.insert(0, newGen0Text)


# Increments to next generation
def incrementGeneration():
        global currentGen
        global lastGenPopList
        global desiredChromosome
        global npGenStats
        global peakFitness

        calcStart = time.time()

        newGenPopList = returnNextGen(individualGenList[currentGen-1].populationList, float(mutationRateEntry.get()), int(popSizeEntry.get()), int(alleleCountEntry.get()))
        
        currentGen = currentGen + 1

        calculateFitness(desiredChromosome, newGenPopList, int(alleleCountEntry.get()))
        
        findReproductionChance(newGenPopList)
        newGenPopList = sortByReprodutionChance(newGenPopList)

        newGen = individualGeneration()
        newGen.meanFitness = meanFitness(newGenPopList)
        newGen.maxFitness = maxFitness(newGenPopList)
        newGen.minFitness = minFitness(newGenPopList)
        newGen.populationList = newGenPopList

        individualGenList.append(newGen)   

        addNPGen(newGen) 

        lbxText = "Generation " + str(currentGen) + ": " + str(newGen.meanFitness)
        genListBox.insert(0, lbxText)

        genText = "Current Generation: " + str(currentGen)
        labelGeneration.config(text=genText)

        averageText = "Average Fitness: " + str(round(newGen.meanFitness, 5))
        labelMeanFitness.config(text=averageText)

        minText = "Min Fitness: " + str(round(newGen.minFitness, 5))
        maxText = "Max Fitness: " + str(round(newGen.maxFitness, 5)) 
        labelMaxFitness.config(text=maxText)
        labelMinFitness.config(text=minText)

        if newGen.maxFitness > peakFitness:
                peakFitness = newGen.maxFitness
                fitnessPeakLabel.config(text=("Peak Fitness (all gens): " + str(round(peakFitness, 8))))
                print("test")
        
        replot()

        calcEnd = time.time()

        opTimeListBox.insert(0, (str(round((calcEnd-calcStart)*1000, 12)) + " ms"))
        
def changedSelection(evt):
        global individualGenList

        w = evt.widget
        index = int(w.curselection()[0])
        
        genIndex = (len(individualGenList) - 1) - index
        selectedGen = individualGenList[genIndex]

        detailedSelectedGenText = "Detailed Stats For Gen: " + str(genIndex)
        labelDetailedStatsFor.config(text=detailedSelectedGenText)

        detailedAverageText = "Average Fitness: " + str(round(selectedGen.meanFitness, 5))
        labelDetailedStatsAverage.config(text=detailedAverageText)

        detailedMinText = "Min Fitness: " + str(round(selectedGen.minFitness, 5))  
        labelDetailedStatsMin.config(text=detailedMinText)
        deatailedMaxText = "Max Fitness: " + str(round(selectedGen.maxFitness, 5))
        labelDetailedStatsMax.config(text=deatailedMaxText)


def stepGenerations():
        for i in range(int(stepCountEntry.get())):
                incrementGeneration()

# Creates the root window
root = Tk()
root.geometry("1280x720")
app = Window(root)

# Placing of GUI widgets
placeLabelAtPos(root, "Enter Population Size", 0, 0, fontSize=16)
popSizeEntry = Entry(root, font=("Helvectica", 12))
popSizeEntry.place(x=210, y=5)
popSizeEntry.insert(0, "100")

placeLabelAtPos(root, "Enter Trait Count", 0, 30, fontSize=16)
alleleCountEntry = Entry(root, font=("Helvectica", 12))
alleleCountEntry.place(x=210, y=35)
alleleCountEntry.insert(0, "64")

placeLabelAtPos(root, "Enter Muatation Rate", 0, 60, fontSize=16)
mutationRateEntry = Entry(root, font=("Helvectica", 12))
mutationRateEntry.place(x=210, y=65)
mutationRateEntry.insert(0, "0.05")

newSimButton = Button(root, text="New Simulation", command=restartSimulation, font=("Helvectica", 12), width=43)
newSimButton.place(x=0, y=100)


individualGenList = newGenList(int(alleleCountEntry.get()), int(popSizeEntry.get()))

nextGenButton = Button(root, text="Next Generation", command = incrementGeneration, font=("Helvectica", 12), width=43)
nextGenButton.place(x=0, y= 265)

generationText = "Current Generation: " + str(currentGen)
labelGeneration = Label(root, text = generationText, font=("Helvectica", 16))
labelGeneration.place(x=0, y=140)

averageFitnessText = "Average Fitness: " + str(round(individualGenList[0].meanFitness, 5))
labelMeanFitness = Label(root, text = averageFitnessText, font=("Helvectica", 16))
labelMeanFitness.place(x=0, y=170)

minFitnessText = "Min Fitness: " + str(round(individualGenList[0].minFitness, 5))
labelMinFitness = Label(root, text = minFitnessText, font=("Helvectica", 16))
labelMinFitness.place(x=0, y=200)

maxFitnessText = "Max Fitness: " +  str(round(individualGenList[0].maxFitness, 5))
labelMaxFitness = Label(root, text = maxFitnessText, font=("Helvectica", 16))
labelMaxFitness.place(x=0, y=230)

placeLabelAtPos(root, "Enter Step Count", 0, 300)
stepCountEntry = Entry(root, font=("Helvectica", 12))
stepCountEntry.place(x=210, y=305)
stepCountEntry.insert(0, "10")

stepGenBtn = Button(root, text="Step Generations", command = stepGenerations, font=("Helvectica", 12), width=43)
stepGenBtn.place(x=0, y=330)

fitnessPeakLabel = Label(root, text=("Peak Fitness (all gens): " + str(round(individualGenList[0].maxFitness, 8))), font=("Helvectica", 16))
fitnessPeakLabel.place(x=0, y=365)

genListBox = Listbox(root, height=29, width = 25, font=("Helvectica", 12))
genListBox.place(x=400, y=50)

placeLabelAtPos(root, "Operation Length (ms)", 90, 400)

opTimeListBox = Listbox(root, height=15, width=43, font=("Helvectica", 12))
opTimeListBox.place(x=0, y=430)

placeLabelAtPos(root, "Generation Fitness List", 402, 0)
placeLabelAtPos(root, "Click to View Detailed Stats", 410, 25, fontSize=12)

gen0 = individualGenList[0]
gen0Text = "Generation 0: " + str(round(individualGenList[0].meanFitness, 10))
genListBox.insert(0, gen0Text)
genListBox.bind('<<ListboxSelect>>', changedSelection)

labelDetailedStatsFor = Label(root, text = "Detailed Stats For Gen: 0", font=("Helvectica", 16))
labelDetailedStatsFor.place(x=395, y= 600)

labelDetailedStatsAverage = Label(root, text = averageFitnessText, font=("Helvectica", 16))
labelDetailedStatsAverage.place(x=395, y=630)

labelDetailedStatsMax = Label(root, text = maxFitnessText, font=("Helvectica", 16))
labelDetailedStatsMax.place(x=395, y=660)

labelDetailedStatsMin = Label(root, text = minFitnessText, font=("Helvectica", 16))
labelDetailedStatsMin.place(x=395, y=690)

restartSimulation()
replot()

root.mainloop()

