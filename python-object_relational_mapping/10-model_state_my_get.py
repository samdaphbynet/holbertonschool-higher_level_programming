#!/usr/bin/python3
"""
    script that prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":

    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Bind the engine to the Base
    Base.metadata.create_all(engine)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with given name
    states = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the results
    if states:
        print(states.id)
    else:
        print("Not found")

    # Close connection and exit program
    session.close()
