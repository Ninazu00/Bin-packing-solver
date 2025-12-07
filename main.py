import culturalAlgorithm

#Backtracking testing
#Important variable definitions
binSize = 10
populationSize = 50
mutationRate = 0.1
totalItems = {}
maxGenerations = 100

totalItems = culturalAlgorithm.initializeTotalItems(3,7,20)
bestBin = culturalAlgorithm.generateBinCulturalAlgorithm(maxGenerations, populationSize, mutationRate, totalItems, binSize)
print("Items in best bin:", bestBin.items)
print("Best bin fill rate:", bestBin.getFillRate(binSize))
binAmount = 0
while totalItems:
    for itemID in bestBin.items.keys():
        totalItems.pop(itemID, None)
    if not totalItems:
        break
    bestBin = culturalAlgorithm.generateBinCulturalAlgorithm(maxGenerations, populationSize, mutationRate, totalItems, binSize)
    binAmount += 1
    print("Items in best bin:", bestBin.items.values())
    print("Best bin fill rate:", bestBin.getFillRate(binSize))
print("Total number of bins used: ", binAmount)