# take an input
user_input = input('Enter Phrase: ')


# conver to uppercase
user_input = user_input.upper()

# define an output
translation = ''

# loop over each character in input
for phrase in user_input:


# replace letters if they are leet
  if phrase == 'A':
    translation += '4'
  elif phrase == 'E':
    translation += '3'  
  elif phrase == 'G':
    translation += '6'  
  elif phrase == 'I':
    translation += '1'  
  elif phrase == 'O':
    translation += '0'  
  elif phrase == 'S':
    translation += '5'  
  elif phrase == 'T':
    translation += '7'  
  else:
    translation += phrase  

#print the translation

print(translation)
