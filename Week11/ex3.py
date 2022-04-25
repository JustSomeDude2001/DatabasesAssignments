from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
table = client['test'].restaurants

if table == None:
	print("FAILED FETCH")
	exit(0)

result = table.delete_one({'borough': 'Manhattan'})
print(f"DELETED RESTAURANTS ON MANHATTAN: {result.deleted_count}")
result = table.delete_many({'cuisine': 'Thai'})
print(f"DELETED THAI RESTAURANTS: {result.deleted_count}")
