#startet Konsole
from mod_scan import scanM
from cmd_scan import scanC
import sys
from termcolor import *
import colorama

#Initalisation
def init():
    global C
    #import modules
    l = scanM()
    sys.path.append("modules")
    i=0
    for m in l[1]:
        exec("from " + l[0][i] + " import "+ l[1][i],globals())
        i= i+1
    #import commands
    C = scanC()
init()
print(C)

while True:
    e = input(">>> ")
    if e.split(" ")[0] in set(C):
        if len(e.split(" ")) == 1:
            exec(C[e]+"()")
        else:
            o = e.split()[0]
            p = e.replace(o+" ", "").replace(" ",",")
            exec(C[o]+"("+p+")" )
    else:
        colorama.init()
        cprint("ERROR: Command not found!","red")
