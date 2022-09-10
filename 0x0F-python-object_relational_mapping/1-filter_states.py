#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
   List all the states start with N in Database

"""
import MySQLdb
import sys


  if __name__ == '__main__':
  args = sys.argv
  if len(args) != 4:
    print("usage: {} username password database_name".format(args[0]))
    exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MYSQLdb.connect(host='localhost', user=username, passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_row = cur.execute("SELECT * FROM WHERE states.name LIKE BINARY/'N%' ORDER BY states.id;")
    row = cur.fetchall()
    for row in rows;
    print(row)
    cur.close()
    db.close()
