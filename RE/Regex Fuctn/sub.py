import re

text = "I like Java"

result = re.sub(r"Java", "Python", text)

print(result)