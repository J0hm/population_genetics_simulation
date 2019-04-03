import random as rand
from genetics import *
from tkinter import *
from math import *


alleleCount = 32
popList = createPopulation(32, alleleCount)
#desiredChromosome = randChromosome(alleleCount)
desiredChromosome = randChromosome(alleleCount)

calculateFitness(desiredChromosome, popList, alleleCount)

print("Desired:   ", desiredChromosome)

findReproductionChance(popList)
popList = sortByReprodutionChance(popList)

chanceSum = 0

for i in range(32):
    print("Chromosome:", popList[i].chromosome, "Fitness:", popList[i].fitness, "Reproduction Chance:", popList[i].reproductionChance)
    chanceSum += popList[i].reproductionChance

print("Chance Sum:", chanceSum)
