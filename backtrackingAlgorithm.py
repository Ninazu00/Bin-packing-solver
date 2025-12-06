def sortItems(itemsList):
    return sorted(itemsList, reverse=True)

def placeItem(item, binIndex, usedBins, binRemainingCapacities):
    usedBins[binIndex].append(item)
    binRemainingCapacities[binIndex] -= item

def removeItem(item, binIndex, usedBins, binRemainingCapacities):
    usedBins[binIndex].remove(item)
    binRemainingCapacities[binIndex] += item

def calculateLowerBound(remainingItems, binCapacity):

    pass


def copyBins(bins):

    pass


def pruneBranch(usedBins, bestSolution, remainingItems, binCapacity):

    pass


def initializeSolution(items, binCapacity):

    pass

def findFeasibleBins(item, binRemainingCapacities):
    indices = []
    for i, remaining in enumerate(binRemainingCapacities):
        if item <= remaining:
            indices.append(i)
    return indices

def backtrack(currentIndex, usedBins, binRemainingCapacities, binCapacity, bestSolution, sortedItemsList):
    # Base case: all items have been placed
    if currentIndex == len(sortedItemsList):
        if len(usedBins) < len(bestSolution):
            bestSolution.clear()
            bestSolution.extend(copyBins(usedBins))
        return

    item = sortedItemsList[currentIndex]

    # Remaining items (including current item) for lower bound pruning
    remainingItems = sortedItemsList[currentIndex:]
    if pruneBranch(usedBins, bestSolution, remainingItems, binCapacity):
        return

    # Try placing in existing bins (all feasible choices)
    feasibleBins = findFeasibleBins(item, binRemainingCapacities)
    for i in feasibleBins:
        placeItem(item, i, usedBins, binRemainingCapacities)
        backtrack(currentIndex + 1, usedBins, binRemainingCapacities,
                  binCapacity, bestSolution, sortedItemsList)
        removeItem(item, i, usedBins, binRemainingCapacities)

    # Try placing in a new bin
    usedBins.append([item])
    binRemainingCapacities.append(binCapacity - item)
    backtrack(currentIndex + 1, usedBins, binRemainingCapacities, binCapacity, bestSolution, sortedItemsList)
    usedBins.pop()
    binRemainingCapacities.pop()


def solveBinPacking(items, binCapacity):

    pass