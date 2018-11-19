#!/usr/bin/env python

import CRUD
import sys
import Constants

def select_action(conn):
    action = input(Constants.MENU_PROMPT)
    selector(action, conn)
    
def selector(selection, conn):
    if selection   == Constants.ADD:
        CRUD.add_entry(conn)
    elif selection == Constants.DELETE:
        CRUD.delete_entry(conn)
    elif selection == Constants.EDIT:
        CRUD.update_entry(conn)
    elif selection == Constants.VIEW:
        CRUD.get_all_entries(conn)
    elif selection == Constants.EXIT:
        sys.exit()
    else:
        select_action(conn)