import random as rand
from genetics import *
from tkinter import *
from math import *


alleleCount = 128
popList = createPopulation(128, alleleCount)
#desiredChromosome = randChromosome(alleleCount)
desiredChromosome = randChromosome(alleleCount)

calculateFitness(desiredChromosome, popList, alleleCount)

print("Desired:   ", desiredChromosome)

for i in range(128):
    print("Chromosome:", popList[i].chromosome, "Fitness:", popList[i].fitness)