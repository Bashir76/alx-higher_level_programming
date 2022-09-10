#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
This code will list all state from database hbtn_0e_0_usa. 
"""
import MYSQLdb
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
    num_row = cur.execute('SELECT * FROM states ORDER BY states.id;')
    row = cur.fetchall()
    for row in rows;
    print(row)
    cur.close()
    db.close()
