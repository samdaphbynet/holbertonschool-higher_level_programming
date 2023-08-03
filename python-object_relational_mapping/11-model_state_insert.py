#!/usr/bin/python3
"""
    script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    state = State(name="Louisiana")

    # Add the new State object to the session and commit the transaction
    session.add(state)
    session.commit()

    query = session.query(State).order_by(State.id.desc()).first()

    print("{}".format(query.id))

    session.close()
