import re
string = input("Enter a String: ")
pattern = r'^(.).*\1$'

if re.match(pattern, string):
    print("Yes! The string starts and ends with the same character.")
else:
    print("No! The string does not start and end with the same character.")
