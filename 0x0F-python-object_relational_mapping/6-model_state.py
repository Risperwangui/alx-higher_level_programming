#!/usr/bin/python3
"""starting linking class to the table"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.formar(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=TRUE)
    Base.metadata.create_all(engine)
