#!/usr/bin/env python

import pymysql
import sys
import CRUD
from db_setup import connect_to_db
from menu import select_action

def setup():
    conn = connect_to_db()
    return conn

def main():
    conn = setup()
    while True:
        select_action(conn)
    

if __name__ == "__main__":
    main()
