import re

text = "My name is Siddhesh and I am 20 years old and I have 2 cats and 1 dog." 

print("b:", re.findall(r"\bcat\b", text))
print("B:", re.findall(r"\Bcat", text))
print("d:", re.findall(r"\d", text))
print("D:", re.findall(r"\D", text))
print("s:", re.findall(r"\s", text))
print("S:", re.findall(r"\S", text))
print("w:", re.findall(r"\w", text))
print("W:", re.findall(r"\W", text))
print("Z:", re.findall(r"am\Z", text))


