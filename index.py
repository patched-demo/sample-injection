import sqlite3

CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    """Fetches data from a database based on a configuration value.
    
    Args:
        value (str): The value to be used in the database query to filter results.
    
    Returns:
        list: A list of tuples representing the rows that match the query criteria.
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
