#!/usr/bin/python3
"""
   This scipt displays arguments all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
  if __name__ == '__main__': 
  args = sys.argv
  if len(args) < 5:
    print("usage: {} username password database_name".format(args[0]))
    exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db = MYSQLdb.connect(host='localhost', user=username, passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_row = cur.execute('SELECT * FROM states WHERE states.name LIKE BINARY/%s ORDER BY states.id;".format(state_name))
    row = cur.fetchall()
    for row in rows;
    print(row)
    cur.close()
    db.close()
