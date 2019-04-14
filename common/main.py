import random as rand
from genetics import *
from tkinter import *
from math import *

# These are constants but cannot be delcared as such in python
# Changing them changes how the basic algorithms function
alleleCount = 32
popSize = 256
mutationChance = 0.05
gen = 0

# The main window class
class Window(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)               
                self.master = master
                self.init_window()

        def init_window(self):
                self.master.title("Genetics Simulation Program")
                self.pack(fill=BOTH, expand=1)

# Class for storing data about whole generations
class individualGeneration():
        def __init__(self):
                self.maxFitness = 0
                self.minFitness = 0
                self.meanFitness = 0


# Places a label with text at x,y. Streamlines this process but is not ideal for every situation, as it does not let you change the value of the label
def placeLabelAtPos(window, labelText, xPos, yPos, fontType = "Helvectica", fontSize = 16):
        newPlacedLabel = Label(window, text = labelText, font=(fontType, fontSize))
        newPlacedLabel.place(x=xPos, y=yPos)


# Sets the screen to the starting screen (gets input values)
def restartSimulation():
        pass

# Finds starting values for algoritms
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

individualGenList.insert(0, gen0)

# Creates the root window
root = Tk()
root.geometry("600x600")
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

generationText = "Current Generation: " + str(gen)
labelGeneration = Label(root, text = generationText, font=("Helvectica", 16))
labelGeneration.place(x=0, y=100)

averageFitnessText = "Average Fitness: " + str(round(gen0.meanFitness, 5))
labelMeanFitness = Label(root, text = averageFitnessText, font=("Helvectica", 16))
labelMeanFitness.place(x=0, y=125)


minMaxFitnessText = "Min/Max Fitness: " + str(round(gen0.minFitness, 5))  + ", " + str(round(gen0.maxFitness, 5)) 
labelMinMaxFitness = Label(root, text = minMaxFitnessText, font=("Helvectica", 16))
labelMinMaxFitness.place(x=0, y=150)

genListBox = Listbox(root, height=28, width = 25, font=("Helvectica", 12))
genListBox.place(x=350, y=50)

placeLabelAtPos(root, "Generation Fitness List", 352, 0)
placeLabelAtPos(root, "Click to View Detailed Stats", 360, 25, fontSize=12)

gen0 = individualGenList[0]
gen0Text = "Generation 0: " + str(round(gen0.meanFitness, 10))
genListBox.insert(0, gen0Text)

root.mainloop()

