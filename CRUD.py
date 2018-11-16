#!/usr/bin/env python

import pymysql
import sys
import Constants

def save_entry(entry, conn):
    with conn.cursor() as cur:
        cur.execute(Constants.CREATE_TABLE_IF_NOT_EXISTS)
        cur.execute(Constants.INSERT_INTO % (entry['name']))
        conn.commit()
        cur.close()

def add_entry(conn):
    name = input(Constants.ENTER_NAME)
    entry = {
        "name": name
        }
    context = ""
    save_entry(entry, conn)
    print (Constants.ENTRY_SAVED)

def get_entry_by_name(conn):
    result = []
    search = input(Constants.ENTER_NAME)

    with conn.cursor() as cur:
        cur.execute(Constants.GET_ENTRY_BY_NAME % (search))
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print (Constants.RESULTS)
        print (result)

def get_all_entries(conn):
    result = []

    with conn.cursor() as cur:
        cur.execute(Constants.SELECT_ALL)
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print (Constants.RESULTS)
        print (result)

def get_entry_by_id(conn):
    result =[]
    userInput = input(Constants.ENTER_ID)

    with conn.cursor() as cur:
        cur.execute(Constants.GET_ENTRY_BY_ID % (userInput))
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print (Constants.RESULTS)
        print (result)
        return userInput

def update_entry(conn):
    userInput = get_entry_by_id(conn)
    id_to_update = int(userInput)
    
    confirm = input(Constants.CONFIRM_UPDATE)
    if confirm == "Y":
        name = input(Constants.UPDATE)

        with conn.cursor() as cur:
            cur.execute(Constants.UPDATE_SELECTED_ENTRY % (name, id_to_update))
            conn.commit()
            cur.close()
    elif confirm == "N":
        print (Constants.CANCEL_UPDATE)


def delete_entry(conn):
    userInput = get_entry_by_id(conn)
    id_to_delete = int(userInput)

    confirm = input(Constants.CONFRIM_DELETE)
    if confirm == "Y":

        with conn.cursor() as cur:
            cur.execute(Constants.DELEETE_SELECTED_ENTRY % (id_to_delete))
            conn.commit()
            cur.close()
    elif confirm == "N":
        print (Constants.CANCEL_DELETE)
        
