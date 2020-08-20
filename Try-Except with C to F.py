while True:
  try:
    celsius = int(input('Enter the temperature in celsius: '))
    break
  except ValueError:
    print("Please enter number as digits")

F = (celsius * 9/5) + 32    

print(f'{F} F')