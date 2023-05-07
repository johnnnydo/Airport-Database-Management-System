#created by Johnny Do
#johnnyhd@uci.edu
#46849652
import p2app.events.continents as continents
import sqlite3
'''This modules is holding the functions for the continent related events'''
def search_continents(connection, event):
    '''This function is going to search for existing continents
    and return a list of the data from the database'''
    search_name = event._name
    search_continent = event._continent_code
    if search_name is not None and search_continent is not None:
        query = 'SELECT * FROM continent WHERE name = ? AND continent_code = ?'
        params = (search_name, search_continent)
    elif search_name is None and search_continent is not None:
        query = 'SELECT * FROM continent WHERE continent_code = ?'
        params = (search_continent,)
    elif search_name is not None and search_continent is None:
        query = 'SELECT * FROM continent WHERE name = ?'
        params = (search_name,)
    cursor = connection.execute(query, params)
    results = cursor.fetchall()

    cursor.close()
    return results

def load_continents(connection, event):
    '''This function is going to use select to load
    a existing continent if the user wants to edit it'''
    continent_id = event._continent_id
    query = 'SELECT * FROM continent WHERE continent_id = ?'
    params = (continent_id,)

    cursor = connection.execute(query, params)
    results = cursor.fetchall()
    return results

def new_continent(connection, event):
    '''This is going to allow the user to create a new continent'''
    cont_namet = event._continent
    cont_code = cont_namet.continent_code
    cont_name = cont_namet.name
    cont_id = cont_namet.continent_id
    if cont_name is None:
        cont_name = ''
    elif cont_code is None:
        cont_code = ''
    cursor = connection.execute('INSERT INTO continent (continent_id, continent_code, name) VALUES(?, ?, ?);', (cont_id, cont_code, cont_name))
    return cont_namet

def edited_continent(connection, event):
    '''This is going to allow the user to edit the loaded continent'''
    cont_namet = event._continent
    cont_code = cont_namet.continent_code
    cont_name = cont_namet.name
    cont_id = cont_namet.continent_id
    if cont_name is None:
        cont_name = ''
    elif cont_code is None:
        cont_code = ''

    query = 'UPDATE continent SET continent_code=?, name=? WHERE continent_id=?'
    params = (cont_code, cont_name, cont_id)

    connection.execute(query, params)
    return cont_namet

