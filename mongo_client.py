import pymongo

# class MongoDocument:
    
#     """Initialize defaults."""
#     def __init__(self, data, database, collection, namespace, operation):
#         self.data = data
#         self.database = database
#         self.collection = collection
#         self.namespace = namespace
#         self.operation = operation

url = "localhost"
port = 27017
database = "influx"
collection = "gitlab"

class MongoDB():

    def __init__(self, collection, database, url, port):
        self.client = pymongo.MongoClient(url, port)
        self.database = self.client[database]
        self.col = self.database[collection]

    def get_valid_item_ids(self):
        return set([item['buff_id'] for item in self.col.find()])

    def get_item(self, buff_id):
        res = self.col.find({'buff_id': buff_id})
        if res.count():
            return res[0]
        else:
            return None

    def insert_item(self, item):
        res = self.col.insert_one(item)
        return res.acknowledged

    def delete_item(self, buff_id):
        res = self.col.delete_one({'buff_id': buff_id})
        return res.acknowledged

    def update_item(self, item):
        res = self.col.replace_one({'buff_id': item['buff_id']}, item)
        return res.acknowledged

    def get_all_items(self, rule=None):
        if rule is None:
            rule = {}
        return self.col.find(rule)

    def get_sorted_items(self, sort, rule=None, limit=0):
        if rule is None:
            rule = {}
        return self.col.find(rule).sort(sort, pymongo.ASCENDING).limit(limit)

    def close(self):
        self.client.close()

    def _clear(self):
        return self.col.delete_many({})

    def get_size(self):
        return self.col.estimated_document_count()


# client = MongoDB(collection, database, url, port)
# prev_valid = client.get_all_items("")
# print(prev_valid)
# emp_rec1 = {
# 		"name":"Mr.Geek",
# 		"eid":24,
# 		"location":"delhi"
# 		}
# client.insert_item(emp_rec1)
# print(client.database)