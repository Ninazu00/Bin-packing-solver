
class Individual:
    def __init__(self,binSize):
        self.fitness = -1
        self.items = {}
        self.binSize = binSize
    def getFillRate(self):
        fillAmount = sum(self.items.values())
        return fillAmount/self.binSize

totalItems = {}
selectedIndividuals = []
beliefs = {"min-bin-fill":0,"top-5-items":[]}
def updateBeliefs(selectedIndividuals,beliefs):
    #Keeps count of how many each item appeared in a solution based on its key
    itemsAppearances = {}
    itemsAppearances = dict.fromkeys(totalItems.keys(),0)
    for key in itemsAppearances:
        for  ind in selectedIndividuals:
            if key in ind.items:
                itemsAppearances[key]+=1
    beliefs["top-5-items"] = sorted(itemsAppearances,key = itemsAppearances.get, reverse = True)[:5]
    minFill = min(value.getFillRate() for value in selectedIndividuals)