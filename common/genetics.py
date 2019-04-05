import random as rand
from math import *

# Main individual class that handles all traits of an individual
class individual():
    def __init__(self, alleles = 8):
        self.chromosome = randChromosome(alleles)
        self.fitness = 0
        self.reproductionChance = 0

# Creates a random bianary chromosome with a length number of alleles 
def randChromosome(length = 8):
    rand.seed()
    chromosome = ""
    for i in range(length):
            chromosome = chromosome + str(rand.randint(0, 1))
    return chromosome

# Creates a population of popSize with alleles number of alleles (traits). 
# Returns the list of individuals
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
    sortedList = sorted(individualList, key = lambda x: x.reproductionChance)
    return sortedList

# Finds the chance for each individiual in individualList to reproduce each reproduction cycle. 
# The total chances add to up to 1, and should be used to iterate reproduction
def findReproductionChance(individualList, roundTo = 10):
    fitnessSum = 0
    for i in range(0, len(individualList)):
        fitnessSum += individualList[i].fitness

    for i in range(0, len(individualList)):
        individualList[i].reproductionChance = round((individualList[i].fitness / fitnessSum), roundTo)

# Chance for a chromosome to mutate 
# Chance for a specifific allele to mutate is mutateChance/chromosomeLength
def mutateChromosome(individual, mutateChance):
    pass

# Independant assortment + 
def produceOffspring(parent1, parent2):
    rand.seed()
    offspringChromosome = ""
    for i in range(0, len(parent1.chromosome)):
        chooseParent = rand.randint(0, 1)

        if chooseParent == 0:
            offspringChromosome = offspringChromosome + parent1.chromosome[i:i+1]
        else:
            offspringChromosome += parent2.chromosome[i:i+1]
    
    return offspringChromosome

# This is a specific choice algorithm thrown quickly together
# It will only work in this specific case where the chances are in order
def weightedChoice(pickList, chanceList):
    for i in range(len(pickList)):
        # Check if sum is greater thanb a random 10 digit decimal from 0 to 1, if not
        # add to sum and check again.
        # Rand int could be from lowest to highest repro chance?
        print("temp")
    pass

def returnNextGen(individualList, mutateChance, populationSize):
    nextGen = []
    chanceList = []

    # Sets lists on chances for weighted choice, same index's
    for i in range(0, len(individualList)):
        chanceList.append(individualList[i].reproductionChance)

    for i in range(0, populationSize):
        parent1 = weightedChoice(individualList, chanceList)
        parent2 = weightedChoice(individualList, chanceList)

    
    return nextGen
    pass

    


    