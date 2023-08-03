#!/usr/bin/python3
"""
    Script that prints the first State object from the database.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Bind the engine to the Base
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Fetch all State objects and sort them by states.id
    states = session.query(State).first()

    # Display the results
    if states is None:
        print("Nothing")
    else:
        print(f"{states.id}: {states.name}")

    # Close the session
    session.close()
