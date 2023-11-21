import time
import utils

with open('main.smort') as f: 
  lines=f.readlines()
  lines = [i.strip() for i in lines]
  
vars={}
keywords=['say','var','read','edit','clear','pause']
for i in range(len(lines)):
  if lines[i][:5]=='!help':
    word=lines[i][6:]
    if word not in keywords and word!='':
      print('Sorry, we do not recognize that keyword.')
    elif word=='':
      print('''Smort Code is a powerful, high level, dynamically typed programming language built around Python and the CPython interpreter.\n It offers several useful features which serve a wide range of features. \t it is currently in development, but is constatnly being worked on.
      ''')
    elif word=='say':
      print('!say is a command to print text to the screen.\n Usage: !say Hello World')
  
  if lines[i][:4]=='!say':
    if lines[i][5:] in vars:
      print(vars[lines[i][5:]])
    else:
      print(lines[i][5:])

  if lines[i][:4]=='!var':
    keyValue=lines[i][5:].split('=')
    vars[keyValue[0]]=keyValue[1]
  
  if lines[i]=='!read':
    #TODO
    pass
  
  if lines[i]=='!edit':
    #TODO
    pass
    
  if lines[i]=='!clear':
    print('\033c')
    
  if lines[i][:6]=='!pause':
    time.sleep(float(lines[i][7:]))
