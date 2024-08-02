from .StorageStrategyTemplate import StorageStrategyTemplate


class LocalStorageStrategy(StorageStrategyTemplate):

    def _read_procedure(self, procedure_path):
        with open(procedure_path) as src:
            return src.read()

    def _read_sql(self, sql_path):
        with open(sql_path) as src:
            return src.read()
