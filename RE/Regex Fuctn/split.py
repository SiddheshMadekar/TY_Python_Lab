import re

text = "Siddhesh,Ritesh;Ashay"

result = re.split(r"[,;]", text)

print(result)