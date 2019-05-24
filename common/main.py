import random as rand
import time
import matplotlib
import matplotlib.animation as animation
from matplotlib import style 
from genetics import *
from tkinter import *
from math import *

style.use('ggplot')
f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)




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


def animate(i):
    pullData = open('sampleText.txt','r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    a.clear()
    a.plot(xar,yar)



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
        

        individualGenList = newGenList(int(alleleCountEntry.get()), int(popSizeEntry.get()))
        currentGen = 0

        genLabelText = "Current Generation: " + str(currentGen)
        labelGeneration.config(text=genLabelText)
        averageLabelText = "Average Fitness: " + str(round(individualGenList[0].meanFitness, 5))
        labelMeanFitness.config(text=averageLabelText)
        newMinMaxFitnessText = "Min/Max Fitness: " + str(round(individualGenList[0].minFitness, 5))  + ", " + str(round(individualGenList[0].maxFitness, 5)) 
        labelMinMaxFitness.config(text=newMinMaxFitnessText)

        genListBox.delete(0, END)
        newGen0Text = "Generation 0: " + str(individualGenList[0].meanFitness)
        genListBox.insert(0, newGen0Text)

# Increments to next generation
def incrementGeneration():
        global currentGen
        global lastGenPopList
        global desiredChromosome

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

        lbxText = "Generation " + str(currentGen) + ": " + str(newGen.meanFitness)
        genListBox.insert(0, lbxText)

        genText = "Current Generation: " + str(currentGen)
        labelGeneration.config(text=genText)

        averageText = "Average Fitness: " + str(round(newGen.meanFitness, 5))
        labelMeanFitness.config(text=averageText)

        minMaxText = "Min/Max Fitness: " + str(round(newGen.minFitness, 5))  + ", " + str(round(newGen.maxFitness, 5)) 
        labelMinMaxFitness.config(text=minMaxText)

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

        detailedMinMaxText = "Min/Max Fitness: " + str(round(selectedGen.minFitness, 5))  + ", " + str(round(selectedGen.maxFitness, 5))
        labelDetailedStatsMinMax.config(text=detailedMinMaxText)



# Creates the root window
root = Tk()
root.geometry("600x340")
app = Window(root)

# Placing of GUI widgets
placeLabelAtPos(root, "Enter Population Size", 0, 0, fontSize=12)
popSizeEntry = Entry(root)
popSizeEntry.place(x=170, y=3)
popSizeEntry.insert(0, "100")

placeLabelAtPos(root, "Enter Allele Count", 0, 20, fontSize=12)
alleleCountEntry = Entry(root)
alleleCountEntry.place(x=170, y=23)
alleleCountEntry.insert(0, "64")

placeLabelAtPos(root, "Enter Muatation Rate", 0, 40, fontSize=12)
mutationRateEntry = Entry(root)
mutationRateEntry.place(x=170, y=43)
mutationRateEntry.insert(0, "0.05")

newSimButton = Button(root, text="New Simulation", command=restartSimulation, font=("Helvectica", 12), width=32)
newSimButton.place(x=0, y=65)


individualGenList = newGenList(int(alleleCountEntry.get()), int(popSizeEntry.get()))


nextGenButton = Button(root, text="Next Generation", command = incrementGeneration, font=("Helvectica", 12), width=32)
nextGenButton.place(x=0, y= 175)

generationText = "Current Generation: " + str(currentGen)
labelGeneration = Label(root, text = generationText, font=("Helvectica", 16))
labelGeneration.place(x=0, y=100)

averageFitnessText = "Average Fitness: " + str(round(individualGenList[0].meanFitness, 5))
labelMeanFitness = Label(root, text = averageFitnessText, font=("Helvectica", 16))
labelMeanFitness.place(x=0, y=125)

minMaxFitnessText = "Min/Max Fitness: " + str(round(individualGenList[0].minFitness, 5))  + ", " + str(round(individualGenList[0].maxFitness, 5)) 
labelMinMaxFitness = Label(root, text = minMaxFitnessText, font=("Helvectica", 16))
labelMinMaxFitness.place(x=0, y=150)

genListBox = Listbox(root, height=14, width = 25, font=("Helvectica", 12))
genListBox.place(x=350, y=50)

placeLabelAtPos(root, "Generation Fitness List", 352, 0)
placeLabelAtPos(root, "Click to View Detailed Stats", 360, 25, fontSize=12)

gen0 = individualGenList[0]
gen0Text = "Generation 0: " + str(round(individualGenList[0].meanFitness, 10))
genListBox.insert(0, gen0Text)
genListBox.bind('<<ListboxSelect>>', changedSelection)

labelDetailedStatsFor = Label(root, text = "Detailed Stats For Gen: 0", font=("Helvectica", 16))
labelDetailedStatsFor.place(x=0, y= 240)

labelDetailedStatsAverage = Label(root, text = averageFitnessText, font=("Helvectica", 16))
labelDetailedStatsAverage.place(x=0, y=265)

labelDetailedStatsMinMax = Label(root, text = minMaxFitnessText, font=("Helvectica", 16))
labelDetailedStatsMinMax.place(x=0, y=290)

root.mainloop()

