#created by Johnny Do
#johnnyhd@uci.edu
#46849652
'''This module is going to hold the region event related functions'''
import sqlite3
def search_regions(connection, event):
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











