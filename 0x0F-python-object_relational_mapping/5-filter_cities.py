#!/usr/bin/python3
# you're in my heart
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
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s", (sys.argv[4],))

    rows = cur.fetchall()
    print(", ".join(data[0] for data in rows))
    cur.close()
    db.close()
