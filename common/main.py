import random as rand
from genetics import *
from tkinter import *
from math import *


alleleCount = 128
popList = createPopulation(64, alleleCount)
#desiredChromosome = randChromosome(alleleCount)
desiredChromosome = randChromosome(alleleCount)

calculateFitness(desiredChromosome, popList, alleleCount)

print("Desired:   ", desiredChromosome)

popList = sortByFitness(popList)

for i in range(64):
    print("Chromosome:", popList[i].chromosome, "Fitness:", popList[i].fitness)