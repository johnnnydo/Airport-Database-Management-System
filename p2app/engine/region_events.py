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
        query = f'SELECT * FROM region WHERE "{region_name}" = name AND "{region_code}" = region_code AND "{local_code}" = local_code;'
    elif region_name is not None and region_code is None and local_code is None:
        query = f'SELECT * FROM region WHERE "{region_name}" = name;'
    elif region_name is None and region_code is not None and local_code is None:
        query = f'SELECT * FROM region WHERE  "{region_code}" = region_code;'
    elif region_name is None and region_code is None and local_code is not None:
        query = f'SELECT * FROM region WHERE "{local_code}" = local_code;'
    elif region_name is not None and region_code is None and local_code is not None:
        query = f'SELECT * FROM region WHERE "{region_name}" = name AND "{local_code}" = local_code;'
    elif region_name is not None and region_code is not None and local_code is None:
        query = f'SELECT * FROM region WHERE "{region_name}" = name AND "{region_code}" = region_code;'
    elif region_name is None and region_code is not None and local_code is not None:
        query = f'SELECT * FROM region WHERE "{region_code}" = region_code AND "{local_code}" = local_code;'
    cursor = connection.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def load_region(connection, event):
    '''This function is going to allow the user to load
    a region to edit'''
    region_id = event._region_id
    query = f'SELECT * FROM region WHERE {region_id} = region_id;'
    cursor = connection.execute(query)
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
        cursor = connection.execute(f'UPDATE region SET region_code = "{region_code}", local_code = "{local_code}", name = "{region_name}", continent_id = {continent_id}, country_id = {country_id}, wikipedia_link = NULL, keywords = NULL WHERE {region_id} = region_id;')
    elif region_wiki is None and region_keywords is not None:
        cursor = connection.execute(f'UPDATE region SET region_code = "{region_code}", local_code = "{local_code}", name = "{region_name}", continent_id = {continent_id}, country_id = {country_id}, wikipedia_link = NULL, keywords = "{region_keywords}" WHERE {region_id} = region_id;')
    elif region_wiki is not None and region_keywords is None:
        cursor = connection.execute(f'UPDATE region SET region_code = "{region_code}", local_code = "{local_code}", name = "{region_name}", continent_id = {continent_id}, country_id = {country_id}, wikipedia_link = "{region_wiki}", keywords = NULL WHERE {region_id} = region_id;')
    elif region_wiki is not None and region_keywords is not None:
        cursor = connection.execute(f'UPDATE region SET region_code = "{region_code}", local_code = "{local_code}", name = "{region_name}", continent_id = {continent_id}, country_id = {country_id}, wikipedia_link = "{region_wiki}", keywords = "{region_keywords}" WHERE {region_id} = region_id;')
    return region_namet















