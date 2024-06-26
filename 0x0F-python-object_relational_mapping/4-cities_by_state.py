#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id
                 ORDER BY cities.id ASC""")
    rows = c.fetchall()
    cities_seen = set()
    for row in rows:
        if row[0] not in cities_seen:
            print(row)
            cities_seen.add(row[0])
    c.close()
    db.close()
