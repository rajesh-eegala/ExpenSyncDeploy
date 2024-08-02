class SQLStatement:
    def __init__(self, statement):
        self.statement = statement
        self.is_latest_statement = False

    def format(self, *args, **kwargs):
        self.statement = self.statement.format(*args, **kwargs)
        return self.statement

    def serialize(self):
        return {
            "statement": self.statement,
            "is_latest_statement": self.is_latest_statement
        }

    @staticmethod
    def deserialize(serialized_object):
        instance = SQLStatement(serialized_object["statement"])
        instance.is_latest_statement = serialized_object["is_latest_statement"]
        return instance
