def user_input():
  day = int(input('Day (0-6)? '))
  if day == 0:
    print('Today is Monday')
  elif day == 1:
    print('Today is Tuesday')
  elif day == 2:
    print('Today is Wednesday')
  elif day == 3:
    print('Today is Thursday')
  elif day == 4:
    print('Today is Friday')
  elif day == 5:
    print('Today is Saturday')
  elif day == 6:
    print('Today is Sunday')
  else:
    print(f'Incorrect input try again.')
    user_input()


user_input()





