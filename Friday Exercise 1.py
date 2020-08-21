# Take a user's input for a number.
# Add a Try and Except to account if User will input a string.

try:
  user_input = int(input('Give me a number from 1-99: '))
except ValueError:
    user_input = int(input('Please enter an Integer (whole number): '))

# A for loop to list the range of the numbers that was inputted. 

for number in range(1, user_input + 1):


# If any number is divisible by 3 and 5 then print "fizzbuzz"

  if number % 3 == 0 and number % 5 == 0:
    print('fizzbuzz')


# If a number is divisible by 3 then print "fizz"

  elif number % 3 == 0:
    print('fizz')


# If a number is divisible by 5 then print "buzz"
  elif number % 5 == 0:
    print('buzz')


  else:
    print(number)
