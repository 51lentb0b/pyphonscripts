import getpass
import sys
import telnetlib

HOST = "192.168.1.1"
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("vlan mytestvlan\n")
tn.write("exit\n")
tn.write("vlan mytetsvlan2\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
