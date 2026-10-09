import re

text = "price is 50rs"
pattern = re.escape("50rs")

result = re.search(pattern, text)

if result:
    print("Found:", result.group())



