#!/usr/bin/python3
"""
    sc
    script that takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument. But this time, write one
    that is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == '__main__':

    # Connect to the Mysql server
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Prepare the SQL query with a placeholder (%s) for the state name
    query = "SELECT * FROM states WHERE name= %s ORDER BY states.id ASC"
    state_name = sys.argv[4]

    # Use the execute method with parameters to pass the state name
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Close the cursor and database
    cursor.close()
    db.close()
