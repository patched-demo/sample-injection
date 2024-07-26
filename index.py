import sqlite3

CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    """
    Fetches data from the default table configured in the CONFIG dictionary where the default column matches the provided value.
    
    Args:
        value str: The value to match against the default column in the default table.
    
    Returns:
        list: A list of tuples containing the rows fetched from the database that match the given value.
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
