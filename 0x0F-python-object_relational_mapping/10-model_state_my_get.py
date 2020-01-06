#!/usr/bin/python3
# Prints the State object with the name passed as argument from the
# database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    usuario = sys.argv[1]
    clave = sys.argv[2]
    bdatos = sys.argv[3]
    estados = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usuario, clave, bdatos), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    res = states.filter_by(name=estados).first()
    print(res.id if res else "Not found")
    session.close()
