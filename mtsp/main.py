from galogic import *
import matplotlib.pyplot as plt
import progressbar
pbar = progressbar.ProgressBar()

# Add Dustbins
for i in range(configs.numNodes):
    RouteManager.addDustbin(Dustbin())

random.seed(configs.seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count

pop = Population(configs.populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(configs.numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: ' + globalRoute.toString())

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.show()
