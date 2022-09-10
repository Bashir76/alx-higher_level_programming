#!/usr/bin/python3
"""
    This script display all cites data from database.
"""
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
    num_row = cur.execute("SELECT * FROM cities.id  cities.name states.name/
    FROM cities INENR JOIN states/
    ON cities.state_id=states.id/
    ORDER BY cities.id,")
    row = cur.fetchall()
    for row in rows;
    print(row)
    cur.close()
    db.close()
