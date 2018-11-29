from random import randint
import datetime
import random
import time
import csv
import string
import re, string
import os
import sys
import re
import numpy as np
from numpy.random import choice
import matplotlib.pyplot as plt
import os
clear = lambda: os.system('cls')


####################################### DEFINE DATA #########################################
Generation = 150
gene = 0,1
mutationRate = 0.008 # /100
pop = random.choices(gene, k=550)
geneLength = 6
crossoverRate = 70
bitMutation = 1
individual = pop[:geneLength]
############################################################################################
population = []
offspring = []
offspringfitness = []
overallfitness = []
fitness = []
rules = []
fit = []
max_fitness = []
max_individual = []
fittest = []
rulesFitness = []



def GeneratePopulation():
    z = 0
    y = 0
    for i in range(0, len(pop), geneLength):
        x = (str(pop[i : i+geneLength]))
        out = re.sub('[%s]' % re.escape(string.punctuation), '', x)
        out = out.replace(' ', '')
        population.append(out)
        f = population[z].count('1')
        fi = (f * 1)
        fitness.append(fi)
        #print ('Individual', z, '-', population[z], 'Fitness', fitness[z],'%')
        z += 1
        y += f
    overallfitness = y*1
    print('Generation:  0')
    print(population)
def selectionandcrossover():
    z = 0
    X = 30
    for i in range(0, (X), geneLength):
        genes = random.choices(population = population, weights = fitness, k=2)
        chance = (random.randint(0,100))
        if chance < crossoverRate:
            child1 = (genes[0][:3] + genes[1][3:6])
            child2 =(genes[1][:3] + genes[0][3:6])
        else:
            child1 = (genes[0])
            child2 = (genes[1])
    #print(child1)
    #print(child2)
        c = (random.randint(0,100))
        if c < mutationRate:
            x = (randint(0,(5)))
            y = (randint(0,(5)))
            mutated_child1 = child1
            mutated_child2 = child2
            i = 0
            for i in range(0, (bitMutation)):
                if (mutated_child1[x] == 1):
                    mutated_child1[x] = 0
                    i +=1
                elif (mutated_child1[x] == 0):
                    mutated_child1[x] = 1
                    i +=1
                if (mutated_child2[y] == 1):
                    mutated_child2[y] = 0
                    i +=1
                elif (mutated_child2[y] == 0):
                    mutated_child2[y] = 1
                    i +=1

            offspring.append(mutated_child1)
            offspring.append(mutated_child2)

        else:
            offspring.append(child1)
            offspring.append(child2)
        z += 1
        z += 1
def offspringfit():
    z = 0
    y = 0
    for i in range(0, len(offspring)):
        f = offspring[z].count('1')
        fi = (f * 1)
        offspringfitness.append(fi)
        #print ('Offspring', z, '-', offspring[z], 'Fitness', offspringfitness[z],'%')
        max_fitness.append(max(offspringfitness))
        max_individual.append(max(offspring))
        z += 1
        y += f
    overallfitness.append(y)
    of = y*1
    del fittest [:]
    fittest.append(max(max_individual))
    offspring.remove(min(offspring))
    offspring.append(fittest)
    del max_individual[:]
    #print('Offspring Overall Fitness', of, '%')
    population == offspring
    fitness == offspringfitness

    del offspring[:]
    del offspringfitness[:]
def cls():
    os.system("cls")
def importRuleBase():
    with open("C:/Users/devon/Documents/Year 3 - UWE/Biocomputation/Biocomputation Assignment/data1.txt") as readingFile:
        reader = csv.reader(readingFile, delimiter=' ')
        next(reader)
        for row in reader:
            x = (str(row))
            out = re.sub('[%s]' % re.escape(string.punctuation), '', x)
            out = out.replace(' ', '')
            rules.append(out)
def conditions():
    z = 0
    i = 0
    #print("population", population)
    while z < len(population):
        if (population[z]) == (rules[i]):
            fit.append(rules[i])
            rules.remove(rules[i])
            i = 0
            z += 1
        else:
            i +=1

        if i == (len(rules)):
            i = 0
            z += 1

def main():
    m = 0
    GeneratePopulation()
    importRuleBase()
    conditions()
    while m < Generation:
        cls()
        selectionandcrossover()
        offspringfit()
        conditions()
        m +=1
        print('Generation: ', m)
        print(population)
        print(fittest, 'fittest')
        rulesFitness.append(len(set(fit)))
        print(len(set(fit)), '/ 32')
        print(len(set(rules)))
        print(rules)
    plt.plot(rulesFitness)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.show()

main()
