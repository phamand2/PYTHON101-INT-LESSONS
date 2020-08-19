ask_for_coin = int(input('How many coins do you want? '))

coin = 0
while coin <= ask_for_coin:
  print(f'You have {coin} coins.')
  ask_for_another= input('Do you want another? ')
  if ask_for_another.lower() == 'yes': 
    coin = coin + 1
  else:
    print('Bye')
    break
