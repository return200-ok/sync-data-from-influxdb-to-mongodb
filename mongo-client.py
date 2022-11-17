import pymongo


class MongoDocument:
    
    """Initialize defaults."""
    def __init__(self, data, database, collection, namespace, operation):
        self.data = data
        self.database = database
        self.collection = collection
        self.namespace = namespace
        self.operation = operation

class MongoClient:
    def __init__(self, DB_URI):
        self.DB_URI = DB_URI
    def client(self):
        if not self._client:
            self._client = MongoClient(DB_URI)
        return self._client

client = pymongo.MongoClient("localhost", 27017)
db = client.test
print(db.name)
print(db.my_collection)
# db.my_collection.insert_one({"x": 10}).inserted_id
# for item in db.my_collection.find():
#     print(item["x"])
# db.my_collection.create_index("x")
# for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
#     print(item["x"])