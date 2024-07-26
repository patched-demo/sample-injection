import sqlite3

CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    """
    Fetches data from the database based on the given configuration value.
    
    Args:
        value str: The value to be matched in the configured column.
    
    Returns:
        list: A list of tuples containing the rows that match the specified value.
    """
    query = "SELECT * FROM " + CONFIG["default_table"] + " WHERE " + CONFIG["default_column"] + " = '" + value + "'"

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    return result

# Test
print(get_data_by_config_value("admin"))
