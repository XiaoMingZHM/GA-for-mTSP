import random
import math
import configparser
'''
Contains all global variables specific to simulation
'''
class singleton_configs:
    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read("global_parameters.ini")
        # Defines range for coordinates when dustbins are randomly scattered
        self.xMax = cfg.getint('random', 'xMax')
        self.yMax = cfg.getint('random', 'yMax')
        self.seedValue = cfg.getint('random', 'seedValue')
        self.numNodes = cfg.getint('random', 'numNodes')
        self.numGenerations = cfg.getint('random', 'numGenerations')
        # size of population
        self.populationSize = cfg.getint('population', 'populationSize')
        self.mutationRate = cfg.getfloat('population', 'mutationRate')
        self.tournamentSize = cfg.getint('population', 'tournamentSize')
        self.elitism = cfg.getboolean('population', 'elitism')
        # number of trucks
        self.numTrucks = cfg.getint('problem', 'numTrucks')

configs = singleton_configs()

def random_range(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

# Randomly distribute number of dustbins to subroutes
# Maximum and minimum values are maintained to reach optimal result
def route_lengths():
    upper = (configs.numNodes + configs.numTrucks - 1)
    fa = upper/configs.numTrucks*1.6 # max route length
    fb = upper/configs.numTrucks*0.6 # min route length
    a = random_range(configs.numTrucks, upper)
    while 1:
        if all( i < fa and i > fb  for i in a):
                break
        else:
                a = random_range(configs.numTrucks, upper)
    return a
