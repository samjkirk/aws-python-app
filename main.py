#!/usr/bin/env python

import pymysql
import sys

REGION = 'eu-west-2b'

rds_host  = "pythondb.cxoycka02hiu.eu-west-2.rds.amazonaws.com"
name = "admin"
password = "password"
db_name = "pythondb"

conn = None

def connect_to_db():
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    return conn

def save_entry(entry, conn):
    with conn.cursor() as cur:
        cur.execute("""create table if not exists test (id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id), name VARCHAR(64));""")
        cur.execute("""insert into test  (name) values('%s')""" % (entry['name']))
        conn.commit()
        cur.close()
        

def add_entry(conn):
    name = input("Enter name: ")
    entry = {
        "name": name
        }
    context = ""
    save_entry(entry, conn)
    print ("Entry saved")

def get_entry_by_name(conn):
    result = []
    search = input("Enter name: ")

    with conn.cursor() as cur:
        cur.execute("""select id, name from test where name = '%s'""" % (search))
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Results...")
        print (result)

def get_all_entries(conn):
    result = []

    with conn.cursor() as cur:
        cur.execute("""select * from test""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Results...")
        print (result)

def get_entry_by_id(conn):
    result =[]
    userInput = input("Enter id: ")

    with conn.cursor() as cur:
        cur.execute("""select id, name from test where id = %s""" % (userInput))
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Selected results...")
        print (result)
        return userInput

def update_entry(conn):
    userInput = get_entry_by_id()
    id_to_update = int(userInput)
    
    confirm = input("Is this the entry you want to update? (Y/N)")
    if confirm == "Y":
        name = input("Enter updated name: ")

        with conn.cursor() as cur:
            cur.execute("""update test set name='%s' where id = %s""" % (name, id_to_update))
            conn.commit()
            cur.close()
    elif confirm == "N":
        print ("Selected entry will not be updated")


def delete_entry(conn):
    userInput = get_entry_by_id()
    id_to_delete = int(userInput)

    confirm = input("Is this the entry you want to delete? (Y/N)")
    if confirm == "Y":

        with conn.cursor() as cur:
            cur.execute("""delete from test where id = %s""" % (id_to_delete))
            conn.commit()
            cur.close()
    elif confirm == "N":
        print ("Selected entry will not be deleted")

def main():
    conn = connect_to_db()
    add_entry(conn)
    add_entry(conn)
    add_entry(conn)
    get_all_entries(conn)
    update_entry(conn)
    delete_entry(conn)


if __name__ == "__main__":
    main()
