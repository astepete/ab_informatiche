# script requiring 2 input parameters
import sys

usage="""Requires two parameters (param1, param2)
Usage: python script.py param1 param2"""

if len(sys.argv) < 3:
  print('The script: ',sys.argv[0],usage)
  sys.exit(0) 
  # exits after help printing
  
# read the two input parameters
param1 = sys.argv[1]
param2 = sys.argv[2]
# output the read parameters
print('''The two parameters  received as inputfor the script are:\n ''',param1, param2)