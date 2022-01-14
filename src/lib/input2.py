#the script takes from the user two input parameters
import sys

while(True):
  print('Please insert an integer number in the range 0-10')
  param1=input()
  if int(param1) in range(11):
    while(True):
      print('Please insert a char parameter in [A,B,C]')
      param2=input()
      if param2 in ['A','B','C']:
        print('Uso i due parametri passati da utente:', param1,param2)
        sys.exit()
      else: print('Try again, please')
  else: print('Try again, please')