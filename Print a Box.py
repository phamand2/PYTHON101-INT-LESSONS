width = int(input('What is the width of the box? '))
height = int(input('What is the height of the box? '))


i = 1
print('*' * width)
while i < height - 2:
  print ('*'  + (' ' * (width-2)) + '*')
  i = i + 1

print("*" * width)