

'''Endpoint 2
#horfun,120,true,a,b
endpoint(str)
    parseEntryInput(str) -> input: EntryInput
        getPriceBreakdown(input.names, input.price) Map()
    updatePriceBreakdown(input.breakdown)

    if !done:
        response with "got your item", next = (this endpoint)
    if done:
        fetchTotalBreakdown(mongoDB)
        response: "herei syour breakdown (breakdown)", next


    enter foodName, price, done, split and done:
'''
class EntryInput:
    def __init__(self, itemName: str, breakdownDict, done: bool):
        this.itemName = itemName
        this.breakdownDict = breakdownDict
        this.isDone = done



def parseEntryInput(input: str) -> Optional[EntryInput]:
    try:
        inputList = input.split(',')
        itemName = inputList[0]
        price = double(inputList[1])
        done = bool(inputList[2])
        names = []
        for i in inputList[3:]:
            names.append(i)
    except:
        return None
    
    breakdowns = getPriceBreakdown(names, price)
    return EntryInput(itemName, breakdowns, done)
    

def getPriceBreakdown(names, price):
    breakdown = dict()
    splitPrice = price / len(names)
    for i in names:
        breakdown[i] = splitPrice
    return breakdown

def updatePriceBreakdown(entry: EntryInput):

def fetchTotalBreakdown(mongoDB):




