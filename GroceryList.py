grocerylist = []


options = '''
Pick an option:
P: Print List
A: Add
R: Remove Item from list 
Q: List done
'''


user_input = input(options)
user_input = user_input.upper()

while len(options) > 0:
  if user_input == 'P':
    print('Grocery List:')
    count = 0
    for grocery in grocerylist:
      print(f'{count}: {grocery}')
      count += 1
    print('Got it!')
  elif user_input == 'A':
    new_item = input('What do you want to add? ')
    if len(new_item) > 0:
      grocerylist.append(new_item)
    else:
      user_input = input(options)
      user_input = user_input.upper()
  elif user_input == 'R':
    count = 0
    for grocery in grocerylist:
      print(f'{count}: {grocery}')
      count += 1
    if len(new_item) > 0:
      remove = int(input('What number do you want to remove? '))
      grocerylist.pop(remove)
  elif user_input == 'Q':
    break   
  else:
    print('Try again')

 
  user_input = input(options)
  user_input = user_input.upper()

print('Happy shopping!')





