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

# Mutates one allele in individual 
def mutateChromosome(individual):
    rand.seed()
    #randAllele = rand.randrange(0, len(individual.chromosome)) 
    randAllele = 5

    strStart = individual.chromosome[0:randAllele]
    strEnd = individual.chromosome[randAllele+1:len(individual.chromosome)]

    if individual.chromosome[randAllele:randAllele+1] == "1":
        strMid = "0"
    else:
        strMid = "1"
    
    newString = strStart + strMid + strEnd

    individual.chromosome = newString
       
    return individual


# Independant assortment + production of offspring from two parents
def produceOffspringChromosome(parent1, parent2):
    rand.seed()
    offspringChromosome = ""
    for i in range(0, len(parent1.chromosome)):
        chooseParent = rand.random()

        if chooseParent > 0.5:
            offspringChromosome = offspringChromosome + parent1.chromosome[i:i+1]
        else:
            offspringChromosome += parent2.chromosome[i:i+1]
    
    return offspringChromosome

# Returns the index of chanceList that was picked. Chances must be from 0 to a number
def weightedChoice(chanceList):
    # Starting values 
    currentSum = chanceList[0]
    rand.seed()
    chosenIndex = 0
    chanceListLength = len(chanceList)

    randFloat = round(rand.uniform(0, sum(chanceList)), 10) # Chances can add to any positive integer, this is used to account for errors that would happen if the range was 0 to 1 due to rounding 

    for j in range(chanceListLength):
        if randFloat <= currentSum:
            chosenIndex = j
            break
        else:
            currentSum += chanceList[j]

    return chosenIndex
        
# Returns the next generation
# IndividualList must be a list of individuals with reproductionChance
def returnNextGen(individualList, mutateChance, populationSize, alleleCount):
    nextGen = []
    chanceList = []
    rand.seed()

    # Sets lists on chances for weighted choice, same index's
    for i in range(0, len(individualList)):
        chanceList.append(individualList[i].reproductionChance)
   

    for i in range(0, populationSize):
        parent1index = weightedChoice(chanceList)
        parent2index = weightedChoice(chanceList)

        parent1 = individualList[parent1index]
        parent2 = individualList[parent2index]

        newIndividual = individual(alleleCount)
        newIndividual.chromosome = produceOffspringChromosome(parent1, parent2)

        randFloat = rand.random()

        if randFloat <= mutateChance:
            newIndividual = mutateChromosome(newIndividual)
        
        nextGen.append(newIndividual)

    return nextGen