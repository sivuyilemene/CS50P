# LOOPS
# print meow 3 times
print("meow")
print("meow")
print("meow")

# This is okay but would be unsustainable
# we need to use a WHILE LOOP
i = 3
while i != 0:
    print("purr")
    i -= 1

# FOR LOOP with Lists
# This is good but is limited to how many values
# you can input into the list
for i in [0, 1, 2]:
    print("lick")

# FOR LOOP with range
# iterates for x-1 in range(x)
for i in range(3):
    print("smell")

# instead of using a variable use "_" as
# a variable that you only use in iterator functions
for _ in range(3):
    print("climb")

# BREAK keyword
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
