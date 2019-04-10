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

# Places a label with text at x,y. Streamlines this process but is not ideal for every situation
def placeLabelAtPos(window, labelText, xPos, yPos, fontType = "Helvectica", fontSize = 16):
        newPlacedLabel = Label(window, text = labelText, font=(fontType, fontSize))
        newPlacedLabel.place(x=xPos, y=yPos)

# Finds starting values for algoritms
popList = createPopulation(popSize, alleleCount)
desiredChromosome = randChromosome(alleleCount)

calculateFitness(desiredChromosome, popList, alleleCount)

findReproductionChance(popList)
popList = sortByReprodutionChance(popList)

# Creates the root window
root = Tk()
root.geometry("600x600")
app = Window(root)

generationText = "Generation: " + str(gen)
placeLabelAtPos(root, generationText, 0, 0)

averageFitness = meanFitness(popList)
averageFitnessText = "Average Fitness: " + str(round(averageFitness, 5))
placeLabelAtPos(root, averageFitnessText, 0, 25)

popMinFitness = minFitness(popList)
minMaxFitnessText = "Min/Max Fitness: " + str(round(minFitness(popList), 5))  + ", " + str(round(maxFitness(popList), 5)) 
placeLabelAtPos(root, minMaxFitnessText, 0, 50)

root.mainloop()

