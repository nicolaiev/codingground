###### Parsing Temperature from DS18B20-ESP8266 #####
###### Shareble here http://goo.gl/hsl3t4 ###########
import requests
## Using Regular Expression Module
import re

## Simulating r.requests.get(....) from ESP8266
## Raw Text from Pastebin
#r=requests.get('http://pastebin.com/raw.php?i=FdSZmLFk')
r=requests.get('http://pastebin.com/raw.php?i=XPLT0qPa')

data=r.text
## Main line with Regex
temps=re.findall(r'(\d{2}[.]\d{4})', data)
list = [(i) for i in data.split(",")]
print(temps)
print(list)
print("#########################################")

total=len(temps)

for x in range(0, total):
  print(temps[x].split())
  print("#########################################")
  value=temps[x].split()

print(temps[0])
print(temps[1])
print("#########################################")

for i in range(1,total+1):
  exec("temp%d = temps[i-1]" % i)
print("temp1",temp1)
print("temp2",temp2)

print("#########################################")

for i in range(1,total+1):
  exec("temp%df = float(temps[i-1])" % i)
print("temp1f",temp1)
print("temp2f",temp2)

print("#########################################")

for i in range(1,total+1):
   exec("print(temp%d)" % i)
print("#########################################")

for i in range(1,total+1):
   exec("print(temp%df)" % i)
print("#########################################")

####################################################
