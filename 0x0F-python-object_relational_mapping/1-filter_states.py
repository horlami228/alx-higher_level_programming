#!/usr/bin/python3

"""
    This is a script that lists all states with a name starting with
    N(upper N)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    my_host = "localhost"
    port = 3306
    my_user = sys.argv[1]
    my_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host=my_host, port=port, user=my_user,
                         password=my_password, database=db_name)

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(sql)
    states = cursor.fetchall()
    for row in states:
        print(row)
