import re


name = input("whats your name ").strip()
# if "," in name:
#   last,first = name.split(", ")
#   name = f"{first} {last}"
# print(f"Hello, {name}")

# Using regex to find first and last name
# pattern = anyname, anylastname
# () is a group and returns the value
# matches = re.search("^(.+), *(.+)$", name)
# if matches:
#     last = matches.group(1)
#     first = matches.groups(2)
#     name = f"{first} {last}"
# print(f"Hello, {name}")

# := 
# operater allows you to ask a boolean question and assign the return value of function
if matches := re.search("^(.+), *(.+)$", name):
    last = matches.group(1)
    first = matches.groups(2)
    name = f"{first} {last}"
print(f"Hello, {name}")