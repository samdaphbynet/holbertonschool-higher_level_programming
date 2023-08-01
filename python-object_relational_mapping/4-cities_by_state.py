#!/usr/bin/python3
"""
    script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':

    # Connect to the Mysql server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Use the execute method with parameters to pass the state name
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities, states
                      WHERE cities.state_id = states.id
                      ORDER BY cities.id ASC""")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database
    cursor.close()
    db.close()
