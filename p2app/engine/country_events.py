#created by Johnny Do
#johnnyhd@uci.edu
#46849652
'''this module is going to hold country related event functions'''
import sqlite3
def search_country(connection, event):
    country_code = event._country_code
    country_name = event._name
    if country_name is not None and country_code is not None:
        query = f'SELECT * FROM country WHERE "{country_code}" = country_code AND "{country_name}" = name;'
    elif country_name is not None and country_code is None:
        query = f'SELECT * FROM country WHERE "{country_name}" = name;'
    elif country_name is None and country_code is not None:
        query = f'SELECT * FROM country WHERE "{country_code}" = country_code;'
    cursor = connection.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results