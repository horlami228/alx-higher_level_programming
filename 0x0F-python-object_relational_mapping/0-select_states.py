#!/usr/bin/python3

"""
    This is a script that list all states
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

    states = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(states)
    result = cursor.fetchall()

    if result is not None:
        for res in result:
            print(res)

        cursor.close()
        db.close()
