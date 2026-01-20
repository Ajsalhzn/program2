import re 
text = "Python is awesome. I love Python programming!"
pattern = r'Python'
replacement = "Java"
new_text = re.sub(pattern, replacement, text)
print("Original Text: \n",text)
print("\nModified Text: \n",new_text)