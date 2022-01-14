def divide(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    print("Division by zero!")
  else:
      print("Result is", result)
  finally:
    print("Executing finally clause\n")

print("Let us divide two integers")
divide(5,3)

print("Let us try division by zero")
divide(2,0)
