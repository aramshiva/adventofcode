with open('input.txt', 'r') as file:
    lines = file.readlines()
n = 0
for line in range(len(lines)):
    num1, num2 = lines[line].strip().split()

    list1 = [int(digit) for digit in num1]
    list2 = [int(digit) for digit in num2]

    for i in range(len(list1)):
        n += abs(list1[i] - list2[i])
    
print(n)
left_numbers = []
right_numbers = []

for line in lines:
    num1, num2 = map(int, line.strip().split())
    left_numbers.append(num1)
    right_numbers.append(num2)

left_numbers.sort()
right_numbers.sort()

total_distance = sum(abs(l - r) for l, r in zip(left_numbers, right_numbers))

print(total_distance)
