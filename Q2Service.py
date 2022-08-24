
mockMongo = dict()
q2Url = "localhost:5000/question2"

class EntryInput:
    def __init__(self, itemName: str, breakdownDict, done: bool):
        self.itemName = itemName
        self.breakdownDict = breakdownDict
        self.isDone = done

def processQ2(input: str, mockMongo):
    entry = parseEntryInput(input)
    if entry is None:
        return ("Validation ERROR!", "")
    else:
        updatePriceBreakdown(entry, mockMongo)
        if entry.done:
            return fetchTotalBreakdown(mockMongo)
        else:
            return ("Enter next item", q2Url)


def parseEntryInput(input: str) -> EntryInput:
    try:
        inputList = input.split(',')
        itemName = inputList[0]
        price = int(inputList[1])
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


def updatePriceBreakdown(entry: EntryInput, mockMongo):
    for i in entry.breakdownDict:
        value = entry.breakdownDict[i]
        if i in mockMongo:
            mockMongo[i] += value
        else:
            mockMongo = i 
    

def fetchTotalBreakdown(mockMongo):
    return mockMongo


input = "horfun,120,true,a,b"
print(processQ2("12,12,false,123,2,2", mockMongo))
print(processQ2(input, mockMongo))





