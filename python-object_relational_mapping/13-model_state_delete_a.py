#!/usr/bin/python3
"""
    script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':

    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Bind the engine to the Base
    Base.metadata.create_all(engine)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a now state object with the given name
    delete = session.query(State).filter(State.name.like('%a%')).all()

    # Display the State
    for state in delete:
        session.delete(state)
    # Commit the transaction
    session.commit()

    session.close()
