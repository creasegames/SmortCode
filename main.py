import os
import time
whiteboard=False
file = open('main.steem','r')
def namer(name):
  name=lines[i]
  name = name[0:len(name)-1]
  return name
lines=[file.readline(),file.readline(),file.readline(),file.readline(),file.readline(),file.readline(),file.readline(),file.readline(),file.readline(),file.readline()]
print(lines)
for i in range(10):
  if lines[i]=='!say\n':
    i+=1
    print(lines[i])
  if lines[i]=='!read\n':
    i+=1
    text = open(namer(lines[i]),'r')
    print(text.read())
    text.close()
  if lines[i]=='!edit\n':
    i+=1
    text = open(namer(lines[i]),'w')
    i+=1
    text.write(lines[i])
    text.close()
  if lines[i]=='!clear\n':
    os.system('clear')
  if lines[i]=='!pause\n':
    i+=1
    time.sleep(float(lines[i]))
