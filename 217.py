n = int(input())

numbers = []
for i in range(n):
    numbers.append(input())

count_three = 0

for num in numbers:
    if numbers.count(num) == 3:
        count_three += 1
        numbers = list(filter(lambda x: x != num, numbers))

print(count_three)
