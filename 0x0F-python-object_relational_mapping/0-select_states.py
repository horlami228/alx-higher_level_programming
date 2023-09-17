#!/usr/bin/python3
import MySQLdb
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server on localhost at port 3306
        connection = MySQLdb.connect(host="localhost", user=username,
                                     passwd=password,
                                     db=database_name, port=3306)

        # Create a cursor for database operations
        cursor = connection.cursor()

        # Execute the SQL query to retrieve states
        # in ascending order by states.id
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Fetch all the rows
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
