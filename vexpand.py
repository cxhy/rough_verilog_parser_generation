#!/usr/bin/python3
import sys
import getopt
import sqlite3
import copy
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)
debug = 1


print ("hello world")

file_name = "test"
file_suffix = "vp"

full_file_name = file_name + '.' + file_suffix
full_file_name_i = full_file_name + '.' + 'i'

with open(full_file_name, 'r') as f:
    data = f.read().splitlines()


if debug == 1:
    pp.pprint(data)

data = [i for i in data if i != '']
data = list(map(str.strip, filter(lambda x:x and x.strip(), data)))

if debug == 1:
    pp.pprint(data)

#print("xxbegin")
#for i in data:
#    if i == "":
#        print("empty")
#    else:
#        print("not empty")
#print("xxend")


#for i in range(len(data)):


#for i in range(len(data)):
#    print("index is ", i)
#    print("and data is ", data[i])

#for i in range(len(data)):
#    print(data[i])


#with open(full_file_name_i,'w') as w:
#    for i in range(len(data)):
#        w.write(i)


#conn = sqlite3.connect('example.db')
#
#c = conn.cursor()
#
#c.execute('''CREATE TABLE stocks
#        (date text, trans text, symbol text, qty real, price real)''')
#
#
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
#conn.commit()
#
#conn.close()



