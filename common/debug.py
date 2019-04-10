import random as rand
from genetics import *
from tkinter import *
from math import *


alleleCount = 32
popList = createPopulation(256, alleleCount)
desiredChromosome = randChromosome(alleleCount)

calculateFitness(desiredChromosome, popList, alleleCount)

print("Desired:   ", desiredChromosome)

findReproductionChance(popList)
popList = sortByReprodutionChance(popList)

chanceSum = 0
chanceList = []

for i in range(0, len(popList)):
        chanceList.append(popList[i].reproductionChance)

for i in range(10):
        print(weightedChoice(chanceList))

print("Mean/Max/Min Fitness:", meanFitness(popList), maxFitness(popList), minFitness(popList))

for i in range(1, 100):
   print("Gen:", i)
   popList = returnNextGen(popList, 0.05, 32, 32)
   calculateFitness(desiredChromosome, popList, alleleCount)
   findReproductionChance(popList)
   popList = sortByReprodutionChance(popList)
   print("Mean/Max/Min Fitness:", meanFitness(popList), maxFitness(popList), minFitness(popList))