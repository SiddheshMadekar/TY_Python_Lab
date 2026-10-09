import numpy as np

data = np.array([
    ('A', 10),
    ('B', 20),
    ('C', 30)
], dtype=[('Label', 'U10'), ('Value', 'i4')])

print(data)
print("Labels:", data['Label'])
print("Values:", data['Value'])