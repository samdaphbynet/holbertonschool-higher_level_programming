#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])

    # Create the cursor queries
    cursor = db.cursor()

    # Execute the query cursor
    cursor.execute("""SELECT cities.name
                      FROM cities
                      JOIN states
                      ON cities.state_id = states.id
                      WHERE states.name = %s""", (sys.argv[4], ))

    # Fetch the and display the results
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(row[0])
    print(", ".join(result))

    # Close the cursor and database
    cursor.close()
    db.close()
