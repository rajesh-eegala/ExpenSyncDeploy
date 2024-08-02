import uuid
from abc import ABC, abstractmethod

class ResultPersistenceStrategy(ABC):
    """
    Class default do nothing.
    """

    def __init__(self):
        self.buffer_id = None
        self.buffer_destination = None

    def change_buffer_id(self):
        self.buffer_id = uuid.uuid4()

    def create_buffer(self):
        self.change_buffer_id()
        return self._init_buffer()

    def flush_buffer(self):
        statements =  self._flush_buffer()
        statements[-1].is_latest_statement = True
        return statements

    @property
    def extra_procedure_variables(self):
        return {
            "__temp_table__": self.temp_table_name
        }

    @property
    def temp_table_name(self):
        return str(self.buffer_id)

    @abstractmethod
    def _init_buffer(self):
        pass

    @abstractmethod
    def _flush_buffer(self):
        pass
