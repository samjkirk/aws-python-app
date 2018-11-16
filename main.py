#!/usr/bin/env python

import pymysql
import sys
import CRUD
from db_setup import connect_to_db

def main():
    conn = connect_to_db()
    CRUD.add_entry(conn)
    CRUD.add_entry(conn)
    CRUD.add_entry(conn)
    CRUD.get_all_entries(conn)
    CRUD.update_entry(conn)
    CRUD.get_all_entries(conn)
    CRUD.delete_entry(conn)
    CRUD.get_all_entries(conn) 

if __name__ == "__main__":
    main()
