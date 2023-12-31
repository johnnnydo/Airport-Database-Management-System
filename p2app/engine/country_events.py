#created by Johnny Do
#johnnyhd@uci.edu
#46849652
'''this module is going to hold country related event functions'''
import sqlite3
def search_country(connection, event):
    '''This takes in a country code and coutry name
    in order to search for a country'''
    country_code = event._country_code
    country_name = event._name
    if country_name is not None and country_code is not None:
        query = 'SELECT * FROM country WHERE country_code = ? AND name = ?'
        params = (country_code, country_name)
    elif country_name is not None and country_code is None:
        query = 'SELECT * FROM country WHERE name = ?'
        params = (country_name,)
    elif country_name is None and country_code is not None:
        query = 'SELECT * FROM country WHERE country_code = ?'
        params = (country_code,)
    cursor = connection.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    return results

def load_country(connection, event):
    '''This function is going to use SELECT to load
    a existing country if the user wants to edit it'''
    country_id = event._country_id
    query = 'SELECT * FROM country WHERE country_id = ?'
    params = (country_id,)
    cursor = connection.execute(query, params)
    results = cursor.fetchall()
    return results

def new_country(connection, event):
    '''This function is going to allow the user to
    save a new country.'''
    country_namet = event._country
    country_id = country_namet.country_id
    country_code = country_namet.country_code
    country_name = country_namet.name
    continent_id = country_namet.continent_id
    country_wiki = country_namet.wikipedia_link
    country_keywords = country_namet.keywords
    if country_code is None:
        country_code = ''
    elif country_name is None:
        country_name = ''
    elif continent_id is None:
        continent_id = ''
    elif continent_id is None:
        continent_id = ''
    elif country_wiki is None:
        country_wiki = ''
    if country_keywords is None:
        cursor = connection.execute('INSERT INTO country(country_id, country_code, name, continent_id, wikipedia_link, keywords) VALUES(?, ?, ?, ?, ?, NULL);', (country_id, country_code, country_name, continent_id, country_wiki))
    elif country_keywords is not None:
        cursor = connection.execute(
            'INSERT INTO country(country_id, country_code, name, continent_id, wikipedia_link, keywords) VALUES(?, ?, ?, ?, ?, ?);',
            (country_id, country_code, country_name, continent_id, country_wiki, country_keywords))

    return country_namet

def edited_country(connection, event):
    '''This function is going to allow the user to edit
    a loaded country'''
    country_namet = event._country
    country_id = country_namet.country_id
    country_code = country_namet.country_code
    country_name = country_namet.name
    continent_id = country_namet.continent_id
    country_wiki = country_namet.wikipedia_link
    country_keywords = country_namet.keywords
    if country_code is None:
        country_code = ''
    elif country_name is None:
        country_name = ''
    elif continent_id is None:
        continent_id = ''
    elif continent_id is None:
        continent_id = ''
    elif country_wiki is None:
        country_wiki = ''
    if country_keywords is not None:
        query = 'UPDATE country SET country_code = ?, name = ?, continent_id = ?, wikipedia_link = ?, keywords = ? WHERE country_id = ?'
        params = (
        country_code, country_name, continent_id, country_wiki, country_keywords, country_id)
        cursor = connection.execute(query, params)
    elif country_keywords is None:
        query = 'UPDATE country SET country_code = ?, name = ?, continent_id = ?, wikipedia_link = ?, keywords = NULL WHERE country_id = ?'
        params = (country_code, country_name, continent_id, country_wiki, country_id)
        cursor = connection.execute(query, params)
    return country_namet
