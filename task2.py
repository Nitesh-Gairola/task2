#! /usr/bin/python3

print("content-type: text/html")
print()




import cgi
import subprocess

mydata = cgi.FieldStorage()
v = mydata.getvalue("c")
o = subprocess.getoutput(v)

print("\n Hello User Welcome to the output Screen")
print("<br/>")
print("<br/>")

print("..................................................................................................................................................................................................................................................................................................................................................................................................")
print("<br/>")
print("<br/>")

print("Your Command is : ",v)

print("<br/>")
print("<br/>")

print("..................................................................................................................................................................................................................................................................................................................................................................................................")
print("<br/>")
print("<br/>")


print(v + "\tis: ",o)  