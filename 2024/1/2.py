from collections import Counter

with open('input.txt', 'r') as file:
    lines = file.readlines()

left_numbers = []
right_numbers = []

for line in lines:
    num1, num2 = line.strip().split()
    left_numbers.append(int(num1))
    right_numbers.append(int(num2))

right_counts = Counter(right_numbers)

total = 0

for num in left_numbers:
    total += num * right_counts.get(num, 0)

print(total)
