print("Enter width")
width = int(input())
print("Enter height")
height = int(input())

for i in range(height):
    if i in[0]:
        print("* "*(width))
    elif i in[(height-1)]:
        print("* "*(width))
    else:
        print("*"+"  "*(width-2)+" *")

input()