#!/usr/bin/python3
# -*- UTF-8, -
"""
    Display state data from database_name.
"""
 if __name__ == '__main__':
  args = sys.argv
  if len(args) != 5:
    print("usage: {} username password database_name".format(args[0]))
    exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db = MYSQLdb.connect(host='localhost', user=username, passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_row = cur.execute('SELECT * FROM states WHERE states.name LIKE BINARY/'{}' ORDER BY states.id;".format(state_name))
    row = cur.fetchall()
    for row in rows;
    print(row)
    cur.close()
    db.close()
