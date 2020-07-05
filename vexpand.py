#!/usr/bin/python3
import sys
import getopt
import sqlite3
import copy
import re
import pprint


verilog_key_words = ('always', 'end', 'ifnone', 'or', 'rpmos', 'tranif1', 'and', 'endcase', 'initial', 'output',
                     'rtran', 'tri', 'assign', 'endmodule', 'inout', 'parameter', 'rtranif0', 'tri0', 'begin',
                     'endfunction', 'input', 'pmos', 'rtranif1', 'tri1', 'buf', 'endprimitive', 'integer', 'posedge',
                     'scalared', 'triand', 'bufif0', 'endspecify', 'join', 'primitive', 'small', 'trior', 'bufif1',
                     'endtable', 'large', 'pull0', 'specify', 'trireg', 'case', 'endtask', 'macromodule', 'pull1',
                     'specparam', 'vectored', 'casex', 'event', 'medium', 'pullup', 'strong0', 'wait', 'casez', 'for',
                     'module', 'pulldown', 'strong1', 'wand', 'cmos', 'force', 'nand', 'rcmos', 'supply0', 'weak0',
                     'deassign', 'forever', 'negedge', 'real', 'supply1', 'weak1', 'default', 'for', 'nmos', 'realtime',
                     'table', 'while', 'defparam', 'function', 'nor', 'reg', 'task', 'wire', 'disable', 'highz0', 'not',
                     'release', 'time', 'wor', 'edge', 'highz1', 'notif0', 'repeat', 'tran', 'xnor', 'else', 'if',
                     'notif1', 'rnmos','tranif0', 'xor')

vamke_key_words = ('ModuleBeg', 'ModuleBegEnd', 'Regs', 'Wires', 'Ports', 'Connect', 'Instance')

verlog_key_expressions = ('{', '}', '+', '-', '*', '/', '%', '<', '>', '<=', '!', '&&', '&', '|', '||', '==', '!=',
                          '===', '!==', '~', '^', '~^', '^~', '~&', '~|', '<<', '>>', '?:', '#', '[', ']', ',')

pp = pprint.PrettyPrinter(indent=4)
debug = 0

data  = []
data2 = []
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
data = list(map(str.strip, filter(lambda i:i and i.strip(), data)))

for i in range(len(data)):
    if("//" in data[i]):
        #data2[i] = re.sub(r"\/\/.*", "", data[i])
        print(data[i])
        #print(data2[i])
    #print(data[i])


#if debug == 1:
#    pp.pprint(data)
comment_type1 = re.compile(r"//[.]*")
comment_flag = 0

print(comment_type1.match("kdsjfkldsjfkl//3dfklgjdfkljg"))

#for i in range(len(data)):
#    #print(data[i])
#    if(re.search(r'(.*)\/\*.*\*\/(.*)', data[i], flags=0)) :
#        print(data[i])
#    else :
#        print(i)

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



