#Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing
b = "Hello, World!"
print(b[2:5]) #from 2 to 5(not incl)

#Modifying
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#f-string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

