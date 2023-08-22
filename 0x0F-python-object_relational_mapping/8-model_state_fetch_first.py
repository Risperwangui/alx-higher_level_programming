#!/usr/binpython3
"""this lists all state objects from the dataa=base"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_instance = session.query(State).order_by(State.id).first()
    if first_instance is not None:
        print("{}: {}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")
    session.close()

