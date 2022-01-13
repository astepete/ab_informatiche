number=23
guess=int(input('Enter an integer:'))

if guess==number:
   #New block starts here
   print('Congratulations, you guesse it.')
   print('(but you do not win any prizes!)')
   #New block ens here
elif guess<number:
  #Another Block
  print('No, it is a little higher than that.')
else:
  print('No, it is a little lower than that')

print('Done')
#This last statement is alwaysexecuted
#after the if statement is executed
