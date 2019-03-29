import random as rand
from math import *

class individual():
    def __init__(self, alleles = 8):
        self.chromosome = randChromosome(alleles)
        self.fitness = 0


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


def calculateFitness(targetChromosome, individualChromosomeList, chromosomeLength):
    for i in range(len(individualChromosomeList)):
        similarities = 0
        counter = 0
        for j in individualChromosomeList[i].chromosome:
            if j == targetChromosome[counter:counter+1]:
                similarities += 1
            counter += 1

        calcFitness = similarities/chromosomeLength
        individualChromosomeList[i].fitness = calcFitness

def maxFitness(individualList): 
    max = 0
    for i in range(len(individualList)):
        if individualList[i].fitness > max:
            max = individualList[i].fitness

    return max


def minFitness(individualList):
    min = 999
    for i in range(len(individualList)):
        if individualList[i].fitness < min:
            min = individualList[i].fitness

    return min

def meanFitness(individualList):


            

