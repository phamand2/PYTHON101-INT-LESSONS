grocerylist = []


options = '''
Pick an option:
P: Print List
A: Add
R: Remove Item from list 
Q: List done
'''

def print_grocerylist():
  # Print the current grocery list
  print('\n\n\nGrocery List:')
  count = 1
  for grocery in grocerylist:
    print(f'{count}: {grocery}')

user_input = input(options)
user_input = user_input.upper()

while len(options) > 0:
  if user_input == 'P':
    print_grocerylist()
    count = 1
    print('\nGot it!\n')
    count =+ 1
  elif user_input == 'A':
    new_item = input('What do you want to add? ')
    if len(new_item) > 0:
      grocerylist.append(new_item)
  elif user_input == 'R':
    for grocery in grocerylist:
      print(f'{count+1}: {grocery}')
    if len(new_item) > 0:
      remove = int(input('What number do you want to remove? '))
      grocerylist.pop(remove-1)
  elif user_input == 'Q':
    break   
  else:
    print('Try again')

 
  user_input = input(options)
  user_input = user_input.upper()

print("\n")
print('Happy shopping!')





