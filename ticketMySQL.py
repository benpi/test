#!/usr/bin/python2.7

import os
import time
import MySQLdb


db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
			user="ben", # your username
			passwd="Fib6rtgvcd", # your password
			db="prorating") # name of the database


# Create Cursor object to execute query
cur = db.cursor()

# I suppose I created already the db 'prorating' and create the user ben:
# GRANT ALL PRIVILEGES ON prorating.* TO 'ben'@'127.0.0.1' IDENTIFIED BY 'MyPassword'
# CREATE DATABASE prorating CHARACTER SET 'utf8';

# Use all the SQL you like
#cur.execute("USE prorating")
#cur.execute("SET NAMES utf8")
cur.execute("DROP TABLE IF EXISTS ticketAirport")

cur.execute("CREATE TABLE ticketAirport ( \
	id int UNSIGNED NOT NULL AUTO_INCREMENT, \
	airport varchar(3) NOT NULL, \
	nrTicket int Not NULL, \
	saleDate datetime DEFAULT NULL, \
	PRIMARY KEY (id)) \
	ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;")

cur.execute("LOCK TABLES ticketAirport WRITE")
sql_file = open('tableTicketAirport.sql',"r")
query = sql_file.read()
cur.execute(query)
cur.execute("UNLOCK TABLES")

#print(cur.execute("SELECT * FROM ticketAirport"))

# print all the first cell of all the rows
# for row in cur.fetchall() :
#	print row[0]

