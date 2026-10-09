import re

pattern = re.compile(r"\d+")
text = "My name is Siddhesh and I am 20 years old."

result = pattern.findall(text)
print(result)