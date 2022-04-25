from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
table = client['test'].restaurants

if table == None:
	print("FAILED FETCH")
	exit(0)

cursor = table.find({'cuisine': 'Indian'})
print(f'INDIAN CUISINE COUNT: {len(list(cursor))}.')

cursor = table.find({'$or': [{'cuisine': 'Indian'}, {'cuisine': 'Thai'}]})
print(f'INDIAN or THAI CUISINE COUNT: {len(list(cursor))}.')

item = table.find_one({'address.street': 'Rogers Avenue', 'address.building': '1115', 'address.zipcode': '11226'})
print(f'RESTAURANTS WITH ADDRESS: {item["name"]}')
