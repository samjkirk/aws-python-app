#!/usr/bin/env python

import CRUD

def select_action(conn):
    action = input("Please enter add/delete/update/view:")
    selector(action, conn)
    
def selector(selection, conn):
    if selection == "add":
        CRUD.add_entry(conn)
    elif selection =="delete":
        CRUD.delete_entry(conn)
    elif selection =="update":
        CRUD.update_entry(conn)
    elif selection =="view":
        CRUD.get_all_entries(conn)
    else:
        select_action(conn)
        
    