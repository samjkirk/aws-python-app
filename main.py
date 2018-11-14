#!/usr/bin/env python

import pymysql
import sys

REGION = 'eu-west-2b'

rds_host  = "pythondb.cxoycka02hiu.eu-west-2.rds.amazonaws.com"
name = "pythondb"
password = "pythondbpassword"
db_name = "pythondb"

ID = 1

def connect_to_db():
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

def save_entry(entry):
    
    with conn.cursor() as cur:
        cur.execute("""insert into test (id, name) values( %s, '%s')""" % (entry['id'], entry['name']))
        cur.execute("""select * from test""")
        conn.commit()
        cur.close()
        

def add_entry():

    name = input("Enter name: ")
    entry = {
        "id": ID,
        "name": name
        }
    context = ""
    save_entry(entry)
    ID += 1
    print ("Entry saved")

def get_entry_by_name():

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

def get_all_entries():

    result = []

    with conn.cursor() as cur:
        cur.execute("""select * from test""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Results...")
        print (result)

def get_entry_by_id():
    input = input("Enter id: ")

    with conn.cursor() as cur:
        cur.execute("""select id, name from test where id = %s""" % (input))
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Selected results...")
        print (result)
        return input

def update_entry():

    input = get_entry_by_id()
    id_to_update = int(input)
    
    confirm = input("Is this the entry you want to update? (Y/N)")
    if confirm == "Y":
        name = input("Enter updated name: ")

        with conn.cursor() as cur:
            cur.execute("""update test set name='%s' where id = %s""" % (name, id_to_update))
            conn.commit()
            cur.close()
    elif confirm == "N":
        print ("Selected entry will not be updated")


def delete_entry():
    input = get_entry_by_id()
    id_to_delete = int(input)

    confirm = input("Is this the entry you want to delete? (Y/N)")
    if confirm == "Y":

        with conn.cursor() as cur:
            cur.execute("""delete from test where id = %s""" % (id_to_delete))
            conn.commit()
            cur.close()
    elif confirm == "N":
        print ("Selected entry will not be deleted")

def main():
    connect_to_db()