#!/usr/bin/python3
"""this lists all state objects from the dataa=base"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, Statw

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for first_instance in session.query(State).filter(State.name.like('%a%')):
        print(first_instance.id, first_instance.name, sep=": ")
