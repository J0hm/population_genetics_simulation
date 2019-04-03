import random as rand
from math import *

class individual():
    def __init__(self, alleles = 8):
        self.chromosome = randChromosome(alleles)
        self.fitness = 0
        self.reproductionChance = 0


def randChromosome(length = 8):
    rand.seed()
    chromosome = ""
    for i in range(length):
            chromosome = chromosome + str(rand.randint(0, 1))
    return chromosome


def createPopulation(popSize, alleles = 8):
    individualList = []
    for i in range(popSize):
        individualList.append(individual(alleles))
    return individualList

# Calculates the fitness of each individual in individualList
def calculateFitness(targetChromosome, individualList, chromosomeLength):
    for i in range(len(individualList)):
        similarities = 0
        counter = 0
        for j in individualList[i].chromosome:
            if j == targetChromosome[counter:counter+1]:
                similarities += 1
            counter += 1

        calcFitness = similarities/chromosomeLength
        individualList[i].fitness = calcFitness

# Returns the max fitness of each individual in individualList
def maxFitness(individualList): 
    max = 0
    for i in range(len(individualList)):
        if individualList[i].fitness > max:
            max = individualList[i].fitness

    return max

# Returns the average fitness of each individual in individualList
def minFitness(individualList):
    min = 999
    for i in range(len(individualList)):
        if individualList[i].fitness < min:
            min = individualList[i].fitness

    return min

# Returns the mean fitness of each individual in individualList
def meanFitness(individualList):
    mean = 0
    for i in range(len(individualList)):
        mean += individualList[i].fitness

    mean /= len(individualList)
    return mean

# Sorts individual by fitness.
# Must be run after calculateFitness, because fitness defaults to zero
def sortByFitness(individualList):
    sortedList = sorted(individualList, key=lambda x: x.fitness, reverse=True)

    return sortedList

# Sorts individualList by reproduction chance. 
# Must be run after findReproductionChance, because reproductionChance defaults to zero
def sortByReprodutionChance(individualList):
    sortedList = sorted(individualList, key = lambda x: x.reproductionChance, reverse = True)
    return sortedList

# Finds the chance for each individiual in individualList to reproduce each reproduction cycle. 
# The total chances add to up to 1, and should be used to iterate reproduction
def findReproductionChance(individualList, round = 10):
    fitnessSum = 0
    for i in range(0, len(individualList)):
        fitnessSum += individualList[i].fitness

    for i in range(0, len(individualList)):
        individualList[i].reproductionChance = round((individualList[i].fitness / fitnessSum), round)
 

    