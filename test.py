# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient

url = "localhost"
port = 27017
try:
	conn = MongoClient(url, port)
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database
db = conn.test

# Created or Switched to collection names: my_gfg_collection
collection = db.my_gfg_collection

emp_rec1 = {
		"name":"Mr.Geek",
		"eid":24,
		"location":"delhi"
		}
emp_rec2 = {
		"name":"Mr.Shaurya",
		"eid":14,
		"location":"delhi"
		}

# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)

print("Data inserted with record ids",rec_id1," ",rec_id2)

# Printing the data inserted
cursor = collection.find()
for record in cursor:
	print(record)
