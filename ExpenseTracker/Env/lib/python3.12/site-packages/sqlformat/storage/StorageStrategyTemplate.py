from abc import ABC, abstractmethod
import json

from sqlformat.helper import sql_helper


class StorageStrategyTemplate(ABC):

    def parse_procedure(self, procedure_path, procedure_variables: dict):
        """
        To download procedure from storage and transform placeholder with value
        """
        procedure_statements = self.get_procedure_statements(procedure_path)
        procedure_variables_keyword = procedure_variables.get('keyword', {})
        procedure_variables_index = procedure_variables.get('index', [])
        for sql_statement in procedure_statements:
            sql_statement.format(*procedure_variables_index, **procedure_variables_keyword)
        return procedure_statements

    def get_procedure_statements(self, procedure_path):
        """
        To download procedure from storage
        """
        content = self._read_procedure(procedure_path)
        sql_procedure = json.loads(content)
        statements = []
        for sql_file in sql_procedure:
            sql_file_content = self._read_sql(sql_file["file"])
            statements += sql_helper.split_statements(sql_file_content)
        return statements



    @abstractmethod
    def _read_procedure(self, procedure_path):
        pass

    @abstractmethod
    def _read_sql(self, sql_path):
        pass


