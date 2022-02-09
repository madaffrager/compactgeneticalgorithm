# "THE BEER-WARE LICENSE" (Revision 42):
# <cmte.igor.almeida@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.

__author__ = 'igor'

from random import random
class DNA:
    def __init__ (self, name, weight ,point):
        self.name   = name
        self.weight = weight
        self.point  = point
        self.contains = False

    def __str__(self):
        return f"Name - {self.name}\Poids - {self.weight}\Valeur - {self.point}\tDans le sac - {self.contains}"

DNA_strand = [
    DNA('Boite a bijoux', 15, 15), 
    DNA('Diplomes', 3, 7),
    DNA('Ordinateur', 2, 10), 
    DNA('Argent', 5, 5), 
    DNA('Livres', 9, 8), 
    DNA('Vetements', 20, 17)
]
class Solution(object):
    """
    A solution for the given problem, it is composed of a binary value and its fitness value
    """
    def __init__(self, value):
        self.value = value
        self.fitness = 0

    def calculate_fitness(self, fitness_function):
        self.fitness = fitness_function(self.value)


def generate_candidate(vector):
    """
    Generates a new candidate solution based on the probability vector
    """
    value = ""

    for p in vector:
        value += "1" if random() < p else "0"

    return Solution(value)


def generate_vector(size):
    """
    Initializes a probability vector with given size
    """
    return [0.5] * size


def compete(a, b):
    """
    Returns a tuple with the winner solution
    """
    if a.fitness > b.fitness:
        return a, b
    else:
        return b, a


def update_vector(vector, winner, loser, population_size):
    for i in range(len(vector)):
        if winner[i] != loser[i]:
            if winner[i] == '1':
                vector[i] += 1.0 / float(population_size)
            else:
                vector[i] -= 1.0 / float(population_size)


def run(generations, size, population_size, fitness_function):
    # this is the probability for each solution bit be 1
    vector = generate_vector(size)
    best = None
    last=""
    # I stop by the number of generations but you can define any stop param
    for i in range(generations):
        # generate two candidate solutions, it is like the selection on a conventional GA
        s1 = generate_candidate(vector)
        s2 = generate_candidate(vector)

        # calculate fitness for each
        s1.calculate_fitness(fitness_function)
        s2.calculate_fitness(fitness_function)

        # let them compete, so we can know who is the best of the pair
        winner, loser = compete(s1, s2)

        if best:
            if winner.fitness > best.fitness:
                best = winner
        else:
            best = winner

        # updates the probability vector based on the success of each bit
        update_vector(vector, winner.value, loser.value, population_size)
        
        print ("generation: %d best value: %s best fitness: %f" % (i + 1, best.value, float(best.fitness)))
        
    lst=[]
    for i in best.value:
            lst.append(i)
    for i in range(6):
        last+=lst[i]+"-"+DNA_strand[i].name+", "
    print ("la solution finale est : ",last)



if __name__ == '__main__':
    def f(x):
        lst=[]
        d=0
        w=0
        for i in x:
            lst.append(i)
        print(lst)
        
        for ind in range(6):
            w+=int(lst[ind])*int(DNA_strand[ind].weight)
            d+=int(lst[ind])*int(DNA_strand[ind].point)
            if w>30:
                d=0
        return d
            
        
    run(300, 6, 100, f)