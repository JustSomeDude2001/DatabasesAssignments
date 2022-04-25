from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
table = client['test'].restaurants

if table == None:
	print("FAILED FETCH")
	exit(0)

item = table.insert_one({
    "address": {
        "building": "1480",
        "coord": [-73.9557413, 40.7720266,],
        "street": "2 Avenue",
        "zipcode": "10075"
    },
    "borough": "Manhattan",
    "cuisine": "Italian",
    "grades": [{
            "date": datetime.fromtimestamp(1412152121),
            "grade": "A",
            "score": 11
    }],
    "name": "Vella",
    "restaurant_id": "41704620"
})

print(f"INSERTED ITEM WITH ID: {item.inserted_id}.")
