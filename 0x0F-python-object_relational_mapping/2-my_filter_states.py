#!/usr/bin/python3
# listening synatra and thinking in her
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
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC"
                .format(sys.argv[4]))
    rows = cur.fetchall()

    for data in rows:
        print(data)
    cur.close()
    db.close()
