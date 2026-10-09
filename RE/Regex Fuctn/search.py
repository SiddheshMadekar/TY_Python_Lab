import re

text = "I like Python"

result = re.search(r"Python", text)

if result:
    print("Found at position:", result.start())