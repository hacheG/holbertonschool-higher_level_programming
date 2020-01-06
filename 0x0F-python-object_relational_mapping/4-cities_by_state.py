#!/usr/bin/python3
# winter is here
import MySQLdb
import sys

if __name__ == '__main__':
    db_host = 'localhost'
    usuario = sys.argv[1]
    clave = sys.argv[2]
    base_de_datos = sys.argv[3]

    db = MySQLdb.connect(host=db_host, user=usuario,
                         password=clave, database=base_de_datos, port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
 JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()

    for data in rows:
        print(data)
    cur.close()
    db.close()
