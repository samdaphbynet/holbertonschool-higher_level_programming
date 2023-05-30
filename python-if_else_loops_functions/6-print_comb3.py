#!/usr/bin/python3
combinition = []
for i in range(10):
    for j in range(i+1, 10):
        combinition.append(f"{i}{j}")
print(", ".join(combinition))
