#!/usr/bin/python3
"""Script that lists all states with a name
   starting with N (upper N) from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3])

    # Create a cursor object to execute queries
    cursor = db.cursor()

    """ Execute the query to filter states with a name
        starting with N (upper N)
    """
    cursor.execute("""SELECT * FROM states
                      WHERE name
                      LIKE 'N%'
                      ORDER BY states.id ASC""")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
