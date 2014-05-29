#!bin/python2.7
# -*-coding:Utf-8 -* 

import os
import glob
import subprocess
import time

fil = glob.glob("/home/ben/ori/oriserver/remote/oridatacenter/PROCESSED/prorating/2014-04/*coupon*")

def localCommand(command):
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout, stderr = proc.communicate()
	return proc.returncode, stdout, stderr

try:
	os.remove('tableTicketAirport.sql')
except OSError:
	pass	

my_file = open('tableTicketAirport.sql', "a")
my_file.write("INSERT INTO ticketAirport (airport, nrTicket, saleDate) VALUES \n")
i = 0
while i< len(fil):
	start_time = time.time()
	command = "awk -F, '{print $3, FILENAME}' "+fil[i]+" | sort | uniq -c | sort -nr | awk -v sq=\"'\" '{print \"(\"sq $2 sq\",\", $1\", \"sq substr($3,length($3)-9,6)sq\"),\"}' "
	code, result, error = localCommand(command)
	my_file.write(result)
	print(i)
	print(time.time()-start_time)
	i += 1

my_file.close()

command = "awk '{print}' tableTicketAirport.sql | sed '$s/,$/;/' " 
code, result, error = localCommand(command)
my_file = open('tableTicketAirport.sql', "w")
my_file.write(result)
my_file.close()



