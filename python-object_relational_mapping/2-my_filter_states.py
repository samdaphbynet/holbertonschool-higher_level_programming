#!/usr/bin/python3
"""
    Script that takes in an argument and display all values
    in the states table of hbtn_0e_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':

    # Connect to Mysql server
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])

    # Create a cursor object to execute queries
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display all values in the table
    # of database where name matches the argument
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
