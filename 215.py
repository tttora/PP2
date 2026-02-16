n = int(input())

names = []
for i in range(n):
    name = input()
    names.append(name)

unique = set(names)
print(len(unique))