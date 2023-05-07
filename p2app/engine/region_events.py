#created by Johnny Do
#johnnyhd@uci.edu
#46849652
'''This module is going to hold the region event related functions'''
import sqlite3


def search_regions(connection, event):
    '''This function is going to allow the search feature
    to work for regions'''
    region_name = event._name
    region_code = event._region_code
    local_code = event._local_code
    #all three is not None
    if region_name is not None and region_code is not None and local_code is not None:
        query = 'SELECT * FROM region WHERE name = ? AND region_code = ? AND local_code = ?'
        params = (region_name, region_code, local_code)
    elif region_name is not None and region_code is None and local_code is None:
        query = 'SELECT * FROM region WHERE name = ?'
        params = (region_name,)
    elif region_name is None and region_code is not None and local_code is None:
        query = 'SELECT * FROM region WHERE region_code = ?;'
        params = (region_code,)
    elif region_name is None and region_code is None and local_code is not None:
        query = 'SELECT * FROM region WHERE local_code = ?;'
        params = (local_code,)
    elif region_name is not None and region_code is None and local_code is not None:
        query = 'SELECT * FROM region WHERE name = ? AND local_code = ?;'
        params = (region_name, local_code)
    elif region_name is not None and region_code is not None and local_code is None:
        query = 'SELECT * FROM region WHERE name = ? AND region_code = ?;'
        params = (region_name, region_code)
    elif region_name is None and region_code is not None and local_code is not None:
        query = 'SELECT * FROM region WHERE region_code = ? AND local_code = ?;'
        params = (region_code, local_code)
    cursor = connection.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    return results


def load_region(connection, event):
    '''This function is going to allow the user to load
    a region to edit'''
    region_id = event._region_id
    query = 'SELECT * FROM region WHERE region_id = ?;'
    params = (region_id,)
    cursor = connection.execute(query, params)
    results = cursor.fetchall()
    return results


def new_region(connection, event):
    '''This function is going to allow the user to create a
    new region'''
    region_namet = event._region
    region_id = region_namet.region_id
    region_code = region_namet.region_code
    local_code = region_namet.local_code
    region_name = region_namet.name
    continent_id = region_namet.continent_id
    country_id = region_namet.country_id
    region_wiki = region_namet.wikipedia_link
    region_keywords = region_namet.keywords

    if region_code is None:
        region_code = ''
    elif local_code is None:
        local_code = ''
    elif region_name is None:
        region_name = ''
    elif continent_id is None:
        continent_id = ''
    elif country_id is None:
        country_id = ''
    if region_wiki is None and region_keywords is None:
        cursor = connection.execute('INSERT INTO region(region_id, region_code, local_code, name, continent_id, country_id, wikipedia_link, keywords) VALUES(?, ?, ?, ?, ?, ?, NULL, NULL);', (region_id, region_code, local_code, region_name, continent_id, country_id))
    elif region_wiki is None and region_keywords is not None:
        cursor = connection.execute('INSERT INTO region(region_id, region_code, local_code, name, continent_id, country_id, wikipedia_link, keywords) VALUES(?, ?, ?, ?, ?, ?, NULL, ?);', (region_id, region_code, local_code, region_name, continent_id, country_id, region_keywords))
    elif region_wiki is not None and region_keywords is None:
        cursor = connection.execute('INSERT INTO region(region_id, region_code, local_code, name, continent_id, country_id, wikipedia_link, keywords) VALUES(?, ?, ?, ?, ?, ?, ?, NULL);', (region_id, region_code, local_code, region_name, continent_id, country_id, region_wiki))
    elif region_wiki is not None and region_keywords is not None:
        cursor = connection.execute('INSERT INTO region(region_id, region_code, local_code, name, continent_id, country_id, wikipedia_link, keywords) VALUES(?, ?, ?, ?, ?, ?, ?, ?);', (region_id, region_code, local_code, region_name, continent_id, country_id, region_wiki, region_keywords))

    return region_namet


def edit_region(connection, event):
    '''This function is going to allow the user to edit
    a exisitng region'''
    region_namet = event._region
    region_id = region_namet.region_id
    region_code = region_namet.region_code
    local_code = region_namet.local_code
    region_name = region_namet.name
    continent_id = region_namet.continent_id
    country_id = region_namet.country_id
    region_wiki = region_namet.wikipedia_link
    region_keywords = region_namet.keywords

    if region_code is None:
        region_code = ''
    elif local_code is None:
        local_code = ''
    elif region_name is None:
        region_name = ''
    elif continent_id is None:
        continent_id = ''
    elif country_id is None:
        country_id = ''
    if region_wiki is None and region_keywords is None:
        query = 'UPDATE region SET region_code = ?, local_code = ?, name = ?, continent_id = ?, country_id = ?, wikipedia_link = NULL, keywords = NULL WHERE region_id = ?;'
        params = (region_code, local_code, region_name, continent_id, country_id, region_id)
        cursor = connection.execute(query, params)
    elif region_wiki is None and region_keywords is not None:
        query = 'UPDATE region SET region_code = ?, local_code = ?, name = ?, continent_id = ?, country_id = ?, wikipedia_link = NULL, keywords = ? WHERE region_id = ?;'
        params = (region_code, local_code, region_name, continent_id, country_id, region_keywords, region_id)
        cursor = connection.execute(query, params)
    elif region_wiki is not None and region_keywords is None:
        query = 'UPDATE region SET region_code = ?, local_code = ?, name = ?, continent_id = ?, country_id = ?, wikipedia_link = ?, keywords = NULL WHERE region_id = ?;'
        params = (region_code, local_code, region_name, continent_id, country_id, region_wiki, region_id)
        cursor = connection.execute(query, params)
    elif region_wiki is not None and region_keywords is not None:
        query = 'UPDATE region SET region_code = ?, local_code = ?, name = ?, continent_id = ?, country_id = ?, wikipedia_link = ?, keywords = ? WHERE region_id = ?;'
        params = (region_code, local_code, region_name, continent_id, country_id, region_wiki, region_keywords, region_id)
        cursor = connection.execute(query, params)
    return region_namet















