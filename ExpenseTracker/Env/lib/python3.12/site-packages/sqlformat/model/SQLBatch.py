
class SQLBatch:
    def __init__(self, storage_strategy, persistence_strategy):
        self._statements = []
        self.result_should_persistence = False
        self.storage_strategy = storage_strategy
        self.persistence_strategy = persistence_strategy

    def _reset(self):
        self._statements = []
        self.result_should_persistence = False

    def result_persistence(self, destination):
        self._statements = []
        for create_buffer_statement in self.persistence_strategy.create_buffer():
            self.add_sql(create_buffer_statement)
        self.persistence_strategy.buffer_destination = destination
        self.result_should_persistence = True

    def add_procedure(self, procedure_path, procedure_variables):
        if self.result_should_persistence:
            procedure_variables = self._set_extra_variable_to_procedure(procedure_variables)
        self._statements += self.storage_strategy.parse_procedure(
            procedure_path,
            procedure_variables
        )

    def _set_extra_variable_to_procedure(self, procedure_variables):
        keyword_variables = procedure_variables['keyword']
        persistence_strategy = self.persistence_strategy
        for key, value in persistence_strategy.extra_procedure_variables.items():
            keyword_variables.setdefault(key, value)
        return procedure_variables

    def add_sql(self, sql):
        self._statements.append(sql)

    def get_statements(self):
        if self.result_should_persistence:
            for flush_buffer_statement in self.persistence_strategy.flush_buffer():
                self.add_sql(flush_buffer_statement)
            statements = self._statements
            self._reset()
            return statements
        return self._statements

    def serialize(self):
        return [statement.serialize() for statement in self.get_statements()]
