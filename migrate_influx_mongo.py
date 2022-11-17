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

data_test = [{
          "result": "_result",
          "table": 24,
          "_start": "2022-11-10T08:22:47.137716+00:00",
          "_stop": "2022-11-17T08:22:47.137716+00:00",
          "_time": "2022-11-15T07:45:50+00:00",
          "_value": "c1d900b7",
          "_field": "commit_id",
          "_measurement": "4",
          "author_email": "admin@example.com",
          "commit_id": "c1d900b706be2c560f959ae5ab84285d1b84efc7",
          "commit_title": "Add new file",
          "created_at": "2022-11-09T07:50:17.000Z",
          "project_name": "d"
     },
     {
          "result": "_result",
          "table": 25,
          "_start": "2022-11-10T08:22:47.137716+00:00",
          "_stop": "2022-11-17T08:22:47.137716+00:00",
          "_time": "2022-11-11T02:56:09+00:00",
          "_value": "c1d900b7",
          "_field": "short_id",
          "_measurement": "4",
          "author_email": "admin@example.com",
          "commit_id": "c1d900b706be2c560f959ae5ab84285d1b84efc7",
          "commit_title": "Add new file",
          "created_at": "2022-11-09T07:50:17.000Z",
          "project_name": "d"
     }
]
data_point = influx_client.query_response_to_json(query)
# print(type(data_point))
for mongo_document in data_point:
    mongo_client.insert_item(mongo_document)
    # print(mongo_document)