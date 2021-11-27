import random

from galogic import *

import matplotlib.pyplot as plt
import progressbar
import json

def solve(data):
    configs.numNodes = data.size
    # Add Dustbins
    RouteManager.clearDustbin()
    for i in range(configs.numNodes):
        RouteManager.addDustbin(Dustbin(data.values[i][1],data.values[i][2]))

    random.seed()
    fittest = [] # Fittest value (distance)

    pop = Population(configs.populationSize, True)
    globalRoute = pop.getFittest()
    print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

    # Start evolving

    for i in range(configs.numGenerations):
        pop = GA.evolvePopulation(pop)
        localRoute = pop.getFittest()
        if globalRoute.getDistance() > localRoute.getDistance():
            globalRoute = localRoute
        fittest.append(localRoute.getDistance())

    print ('Global minimum distance: ' + str(globalRoute.getDistance()))
    print ('Final Route: ' + globalRoute.toString())

    return fittest


if __name__ == '__main__':
    result = {}

    from data.instances import instance_list, instance
    for data_file in instance_list:
        record = {}
        data = instance("../data/" + data_file)
        print(data)
        for i in range(30):
            ret = solve(data)
            record[f"{i}"] = ret
        result[data_file] = record
    with open('test.json', 'w') as f:
        json.dump(result, f, indent = 4) # 编码JSON数据

