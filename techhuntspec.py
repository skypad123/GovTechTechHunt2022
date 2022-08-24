

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
    def __init__(self, itemName: str, breakdown: dict<str, double>, done: bool):
        this.itemName = itemName
        this.breakdown = breakdown
        this.isDone = done



def parseEntryInput(input: str) -> EntryInput


def getPriceBreakdown(names: str, price: double) -> dict()<str, double>


def updatePriceBreakdown(entry: EntryInput) -> None (This should call DB for interaction)

def fetchTotalBreakdown(mongoDB)

def returnSuccess



