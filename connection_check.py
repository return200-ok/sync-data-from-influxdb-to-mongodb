from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException

# class Influxchecker:
#     """Initialize defaults."""
#     def __init__(self, client, bucket, org):
#         self.client = client
#         self.bucket = bucket
#         self.org = org


def check_connection():
    """Check that the InfluxDB is running."""
    print("> Checking connection ...", end=" ")
    # self.client = client
    client.api_client.call_api('/ping', 'GET')
    print("ok")


    def check_query(self, client, bucket, org):
        """Check that the credentials has permission to query from the Bucket"""
        print("> Checking credentials for query ...", end=" ")
        self._client = client
        self.bucket = bucket
        self.org = org
        try:
            client.query_api().query(f"from(bucket:\"{bucket}\") |> range(start: -1m) |> limit(n:1)", org)
        except ApiException as e:
            # missing credentials
            if e.status == 404:
                raise Exception(f"The specified token doesn't have sufficient credentials to read from '{bucket}' "
                                f"or specified bucket doesn't exists.") from e
            raise
        print("ok")


    def check_write(self, client, bucket, org):
        """Check that the credentials has permission to write into the Bucket"""
        print("> Checking credentials for write ...", end=" ")
        self.client = client
        self.bucket = bucket
        self.org = org
        try:
            client.write_api(write_options=SYNCHRONOUS).write(bucket, org, b"")
        except ApiException as e:
            # bucket does not exist
            if e.status == 404:
                raise Exception(f"The specified bucket does not exist.") from e
            # insufficient permissions
            if e.status == 403:
                raise Exception(f"The specified token does not have sufficient credentials to write to '{bucket}'.") from e
            # 400 (BadRequest) caused by empty LineProtocol
            if e.status != 400:
                raise
        print("ok")


