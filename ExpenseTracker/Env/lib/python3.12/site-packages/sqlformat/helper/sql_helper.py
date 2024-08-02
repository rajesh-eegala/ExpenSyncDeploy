from sqlformat.model.SQLStatement import SQLStatement

def split_statements(sql_file_content):
    statements = []
    file_statements = sql_file_content.split(";\n")
    for index, file_statement in enumerate(file_statements):
        file_statement = file_statement.strip()
        if len(file_statement) == 0:
            continue
        is_latest_statement = index == len(file_statements) - 1
        if not file_statement.endswith(';'):
            file_statement = file_statement + ';'
        statement = SQLStatement(file_statement)
        statement.is_latest_statement = is_latest_statement
        statements.append(statement)
    return statements