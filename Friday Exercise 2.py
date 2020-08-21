user_input = int(input('Please enter a whole number: '))

a = 0
b = 1

for number in range(user_input):
    print(b)
    a,b = b,a+b