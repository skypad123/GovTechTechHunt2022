from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/")
def endPointChecker():
    with open("data.json", "w") as write_file:
        json.dump({}, write_file)
    return "<p>Endpoint is Live and json file for api is reset.</p>"

@app.route('/one', methods = ['POST'])
def one():
   # CODE
    if request.method == "POST":
        
        with open("data.json", "r") as read_file:
            jsonData = json.load(read_file)

        if request.data.decode() != ""  or "names" in jsonData.keys(): 
            messageString = request.data.decode()
            jsonData = {
                "names": [item.strip() for item in messageString.split(",")]
            }
            with open("data.json", "w") as write_file:
                json.dump(jsonData, write_file)
                
            customString = ",".join([item + "-0/1" for item in jsonData["names"]])
            return{
                "message": f"enter the food items inform to be split and its price one by one (all food items to be unique, in the format 'food-item-name,total-food-item-price,{customString}' where 0/1 for each person indicates if they are participating in spliting) ? current item in list : 0. To end adding food item, enter 'Done' into body.",
                "next": "http://localhost:5000/two"
            }

        else: 
            return {
                "message": "can you list the names involved in the bill split (all name needs to be unique, seperated by comma ie 'anna,betty,chalice' and ended off with a backslash '/') ?", 
                "next": "http://localhost:5000/one"
            }


@app.route('/two', methods = ['POST'])
def two():

    if request.method == "POST":

        with open("data.json", "r") as read_file:
            jsonData = json.load(read_file)

        messageString = request.data.decode().strip()
        print(messageString)

        if not "names" in jsonData.keys():
            return {
                "message": "can you list the names involved in the bill split (all name needs to be unique, seperated by comma ie 'anna,betty,chalice' and ended off with a backslash '/') ?", 
                "next": "http://localhost:5000/one"
            }

        elif "foodItems" not in jsonData.keys() and messageString == "Done":
            return{
                "message": "no food items have been enter into list, all pay $0",
            }


        elif "foodItems" in jsonData.keys() and messageString == "Done": 
            splitDict = {}
            for x in jsonData["names"]:
                splitDict[x] = 0
                
            for x in jsonData["foodItems"]:
                personListLen = len(x["personList"])
                for y in x["personList"]:
                    splitDict[y] += float(x["price"])/personListLen


            customString = ", ".join ([ f"{name} - ${splitDict[name]}" for name in jsonData["names"] ])

            return{
                    "message": f"bill to be be split in the following manner: {customString}",
                }

        elif messageString  != "": 
                foodItemProps = [item.strip() for item in messageString.split(",")]
                personList = []
                for x in enumerate(foodItemProps[2:]):
                    if x[1] == "1":
                        personList.append(jsonData["names"][x[0]])

                if "foodItems" not in jsonData.keys():
                    jsonData["foodItems"] = [
                        { 
                            "name": foodItemProps[0],
                            "price": float(foodItemProps[1]),
                            "personList" : personList
                        }
                    ]
                else: 
                    jsonData["foodItems"].append(
                        { 
                            "name": foodItemProps[0],
                            "price": float(foodItemProps[1]),
                            "personList" : personList
                        }
                    )

                with open("data.json", "w") as write_file:
                    json.dump(jsonData, write_file)
                    
                count = len(jsonData["foodItems"])
                customString = ",".join([item + "-0/1" for item in jsonData["names"]])
                return{
                    "message": f"enter the food items inform to be split and its price one by one (all food items to be unique, in the format 'food-item-name,total-food-item-price,{customString}') ? current item in list : {count}. To end adding food item, enter 'Done' into body.",
                    "next": "http://localhost:5000/two"
                }
        

if __name__ == '__main__':
    app.run()