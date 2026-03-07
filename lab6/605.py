a = input()
vow = ["a", "e", "i", "u", "o", "A", "E", "I", "U", "O"]
s = any(x in vow for x in a)
if s:
    print("Yes")
else:
    print("No")    