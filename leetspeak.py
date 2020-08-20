#Given a paragraph of text as a String, print the paragraph in leetspeak. It's a "clever" way to sound like a "hacker".

#To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

replacements = ( ('A','4'), ('E','3'), ('G','6'), ('I','1'), ('O','0'), ('S','5'), ('T','7') )
my_string = "apple is good for you"
new_string = my_string.upper()
for old, new in replacements:
    new_string = new_string.replace(old, new)

print(new_string)


