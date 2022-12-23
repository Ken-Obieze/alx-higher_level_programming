#!/usr/bin/python3
""" Module that displays all values in state matching an argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    cont = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    cursor = cont.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (sys.argv[4],)
        )
    db = cursor.fetchall()
    for i in db:
        print(i)
