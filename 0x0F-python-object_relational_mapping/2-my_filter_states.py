#!/usr/bin/python3

"""
    This script takes in an argument and displays all values that
    matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
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

    sql = "SELECT * FROM states WHERE states.name = '{}' " \
          "ORDER BY states.id".format(sys.argv[4])
    cursor.execute(sql)
    searched_state = cursor.fetchall()

    for state in searched_state:
        print(state)
