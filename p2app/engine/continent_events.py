#created by Johnny Do

def search_continents(connection, event):
    '''This function is going to search for existing continents
    and return a list of the data from the database'''
    search_name = event._name
    search_continent = event._continent_code
    if search_name is not None and search_continent is not None:
        query = f'SELECT * FROM continent WHERE "{search_name}" = name AND "{search_continent}" = continent_code;'
    elif search_name is None and search_continent is not None:
        query = f'SELECT * FROM continent WHERE "{search_continent}" = continent_code;'
    elif search_name is not None and search_continent is None:
        query = f'SELECT * FROM continent WHERE "{search_name}" = name;'
    cursor = connection.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def load_continents(connection, event):
    continent_id = event._continent_id
    query = f'SELECT * FROM continent WHERE "{continent_id}" = continent_id'
    cursor = connection.execute(query)
    results = cursor.fetchall()
    return results