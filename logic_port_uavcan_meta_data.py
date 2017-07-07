# Reads CAN logs from *.csv files from LogicPort (http://www.pctestinstruments.com/deutsch/downloads.htm) 

# Outputs UAVCAN metadata

# Author: fabolhak

import csv
import re
import os
import sys

# get csv file path as argument
path = ""
if os.path.exists(sys.argv[1]):
    path = os.path.abspath(sys.argv[1])
else:
    print("Cannot find " + sys.argv[1])
    exit()


with open(path, 'rb') as csvfile:
    # read CSV file
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    data_bytes_left = -1
    
    # loop over all rows in CSV file
    for row in reader:
        
        # count down if CAN coloumn has an entry
        if not not row['CAN']:
            data_bytes_left-=1
            
        # check for identifier in CAN coloumn
        if re.match("D:+",row['CAN']) :
            print "new message found:"
            identifier = bin(int(row['CAN'][2:]))[2:]
            print "  identifier raw =",identifier
            print "  priority =",int(identifier[0:5],2)
            print "  message type ID =",int(identifier[5:21],2)
            print "  service =",identifier[21]
            print "  source node ID =",int(identifier[22:29],2) 
            
        # check for data length in CAN coloumn and set data bytes left  
        if re.match("L:+",row['CAN']) :
            print "  data length =",int(row['CAN'][2:])
            data_bytes_left = int(row['CAN'][2:])
            
        # check if we arrived at last data byte (tailbyte)    
        if data_bytes_left==0 :
            data_bytes_left=-1
            tail_byte=bin(ord(row['CAN']))[2:]
            print "  tailbyte raw =",tail_byte
            print "  start of transfer =",tail_byte[0]
            print "  end of transfer =",tail_byte[1]
            print "  toogle byte =",tail_byte[2]
            print "  transfer ID =",int(tail_byte[3:],2)
            
        # check for checksum in CAN coloumn
        if re.match("C:+",row['CAN']) :
            print "  checksum =",int(row['CAN'][2:])
