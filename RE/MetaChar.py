import re

text = "Hii I am Siddhesh"

print("^ :", re.findall(r"^Hii", text))
print("$ :", re.findall(r"Siddhesh$", text))
print("\\ :", re.findall(r"\w", text))
print("[] :", re.findall(r"[aeiou]", text))
print(". :", re.findall(r"H..", text))
print("| :", re.findall(r"Hii|Hello", text))
print("? :", re.findall(r"Siddhesh?", text))
print("* :", re.findall(r"Hi*", text))
print("+ :", re.findall(r"Hi+", text))
print("{} :", re.findall(r"\w{3}", text))
print("() :", re.findall(r"(I am) (Siddhesh)", text))