import datetime
import logging
import os
from datetime import datetime, timedelta
from time import time

from influx_client import InfluxClient, InfluxPoint
from mongo_client import MongoDB

influx_token = os.getenv('INFLUX_TOKEN')
influx_server = os.getenv('INFLUX_DB')
org_name = os.getenv('INFLUX_ORG')
bucket_name = os.getenv('BUCKET_NAME')
measurement = os.getenv('MEASUREMENT')

collection = os.getenv('MONGO_COLLECTION')
database = os.getenv('MONGO_DATABASE')
url = os.getenv('MONGO_URL')
port = int(os.getenv('MONGO_PORT'))

query = 'from(bucket: "gitlab") |> range(start: -7d)'
influx_client = InfluxClient(influx_server, influx_token, org_name, bucket_name)
mongo_client = MongoDB(collection, database, url, port)

data_point = influx_client.query_response_to_json(query)
for mongo_document in data_point:
    mongo_client.insert_item(mongo_document)
