import json

from sqlformat.storage.StorageStrategyTemplate import StorageStrategyTemplate


class InMemoryProcedureStorageStrategy(StorageStrategyTemplate):

    def __init__(self, sql_storage_strategy):
        self.read_sql_strategy = sql_storage_strategy

    def _read_procedure(self, sql_paths):
        """Procedure stored in memory rather stored in file.
        Example input : _read_procedure([
            {
                "file": "./tests/fixture/sql/hello01.sql"
            },
            {
                "file": "./tests/fixture/sql/hello02.sql"
            }
        ])
        """
        return json.dumps(sql_paths)

    def _read_sql(self, sql_path):
        return self.read_sql_strategy._read_sql(sql_path)
