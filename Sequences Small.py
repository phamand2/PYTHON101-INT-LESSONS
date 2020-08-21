#1 Create a list of numbers, print their sum.

numbers = [1, 2, 3, 4, 5]
print('The sum of the list is: ', sum(numbers))

#2 Create a list of numbers, print the largest of the numbers.

numbers = [1, 2, 3, 4, 5]
print('Largest number is:', max(numbers))

#3 Create a list of numbers, print the smallest of the numbers.

numbers = [1, 2, 3, 4, 5]
print('Smallest number is:', min(numbers))

#4 Create a list of numbers, print each number in the list that is even.
even_numbers = []

numbers = [1, 2, 3, 4, 5]
for number in numbers:
  if number % 2 == 0:
    (even_numbers.append(number))
print('Even numbers are ', even_numbers)

#5 Create a list of numbers, print each number in the list that is greater than zero

num_greater_0 = []

mix_numbers = [-1, -2, 0 , 1, 2]
for positive_num in mix_numbers:
  if positive_num > 0:
    (num_greater_0.append(positive_num))
print('The numbers greater than zero are :', num_greater_0)

#6 Create a list of numbers, create a new list which contains every number in the given list which is positive.

num_positive = []

mix_numbers_2 = [-1, -2, 0 , 1, 2, 31]

for positive_num in mix_numbers_2:
  if positive_num >= 0:
    (num_positive.append(positive_num))
print('Numbers that are positive are: ', num_positive)

#7 Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.


factor = 5
a_list = [1, 2, 4, 1, 42]

multiplied_list = [element * factor for element in a_list]

print('Each element multiply by "factor of 5" is: ', multiplied_list)

#8 Given a string, print the string reversed.

string_1 = "Hello World"
print('The reverse order of Hello World is: ',string_1[::-1])
