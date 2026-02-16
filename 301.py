n = input()
isvalid = False
for digit in n:
    if int(digit) % 2 == 0:
        isvalid = True
    else:
        isvalid = False
        break

if isvalid:
    print("Valid")
else:
    print("Not valid")