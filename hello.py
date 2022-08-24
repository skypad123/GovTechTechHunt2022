from flask import Flask
from pymongo import MongoClient
import pymongo
app = Flask(__name__)


test = {
    'id': 1,
    'names': {}
}

@app.route("/")
def hello_world():
    database = get_database()
    bills_collection = database["bill"]
    bills_collection.insert_one(test)
    bill_details = bills_collection.find_one(sort=[( '_id', pymongo.DESCENDING )])
    test['names']['a'] = 1

    filter1 = { 'id': 1 }
    newvalues = { "$set": { 'names.a': 1 } }
    bills_collection.update_one(filter1, newvalues)
    print(bill_details)
    bill_details = bills_collection.find_one(sort=[( '_id', pymongo.DESCENDING )])
    print(bill_details)
    return "<p>Hello, World!</p>"

@app.route('/one', methods = ['POST'])
def one():
   # CODE
    content_type = request.headers.get('Content-Type')
    # if (content_type == 'application/json'):
    #     json = request.json
    #     return json
    # else:
    content = request.data.decode('utf-8')
    raw = content.split(',')
    number = raw[0]
    people = raw[1 : len(raw)]
    print(raw)

    peopleDict = {}
    for i in people:
        if i not in peopleDict:
            peopleDict[i] = 0
    
    database = get_database()
    bills_collection = database["bill"]
    filter1 = { 'id': 1 }
    newvalues = { "$set": { 'names':peopleDict } }

    output = {"message": "Input Received", "next": "http://localhost:5000/two"}
    return output



def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://govtech:fas4gek17DqoXuTs@cluster0.gr7mo0d.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['govtech']


if __name__ == '__main__':
    app.run()