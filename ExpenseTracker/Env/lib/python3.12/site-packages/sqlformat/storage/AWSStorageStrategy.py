import os
import tempfile
from urllib.parse import urlparse

from sqlformat import StorageStrategyTemplate


class AWSStorageStrategy(StorageStrategyTemplate):
    def __init__(self, boto_client):
        self.boto_client = boto_client

    def _read_procedure(self, procedure_path):
        return self.__read_file(procedure_path)

    def _read_sql(self, sql_path):
        return self.__read_file(sql_path)

    def __read_file(self, file_path):
        s3_object = parse_s3_path(file_path, self.boto_client)
        return s3_object.get()["Body"].read().decode('utf-8')

def parse_s3_path(s3_path, boto_client):
    s3_path_info = urlparse(s3_path)
    s3_bucket = s3_path_info.netloc
    s3_path = s3_path_info.path[1:]
    return boto_client.Object(s3_bucket, s3_path)