import os
import time
file = open('main.smort','r')
def namer(name):
  name=lines[i]
  name = name[0:len(name)-1]
  return name
lines=[file.readlines()]

for i in lines:
  i=i.strip()

for i in range(10):
  if lines[i]=='!say\n':
    i+=1
    print(lines[i])
  if lines[i]=='!read':
    i+=1
    text = open(namer(lines[i]),'r')
    print(text.read())
    text.close()
  if lines[i]=='!edit':
    i+=1
    text = open(namer(lines[i]),'w')
    i+=1
    text.write(lines[i])
    text.close()
  if lines[i]=='!clear':
    os.system('clear')
  if lines[i]=='!pause':
    i+=1
    time.sleep(float(lines[i]))
