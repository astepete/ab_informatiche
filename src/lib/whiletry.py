number=23
running=True

while running:
  guess=int(input('Enter an integer:'))
  if guess==number:
    print('Congratulations, you guessed it.')
    #This causes the while loop to stop
    running=False
  elif guess<number:
    print('No, it is a little higherthan that.')
  else:
    print('No, it is a little lower than that')
else:
  print('The while loop is over.')

print('Done')