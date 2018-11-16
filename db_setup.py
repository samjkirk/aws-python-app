#!/usr/bin/env python

import pymysql
import sys
import Constants

REGION = Constants.REGION

rds_host  = Constants.RDS_HOST
name = Constants.USER_NAME
password = Constants.PASSWORD
db_name = Constants.DB_NAME

def connect_to_db():
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    return conn
