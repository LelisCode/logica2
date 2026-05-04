n = []

import math 
for i in range(1, 11):
    num = float(input(f"Digite o número {i}: "))
    n.append(num)


s = sum(n)
m = s / len(n)
mr = max(n)
mn = min(n)
mu = math.prod(n)


print("-" * 50)
print("NÚMEROS")
print(f"\nSoma: {s:.2f}")
print(f"\nMédia {m:.2f}")
print(f"\nMaior {mr:.2f}")
print(f"\nMenor {mn:.2f}")
print(f"\nMultiplicação{mu:.2f}")
print("-" * 50)