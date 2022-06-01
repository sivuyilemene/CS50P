# Write File
# name = input("whats your name? ")


# with open("name.txt", "a") as file:
#     file.write(f"{name}\n")
    # file.close()


# Read File
# with open("name.txt", "r") as file:
#   lines = file.readlines()

# print each line in file
# for line in lines:
#   print("hello,", line.rstrip())
  
#  print each line in file but better
# with open("name.txt", "r") as file:
#    for line in file:
#      print("hello," , line.rstrip())

# Print sorted lines from file

names = []

with open("nam.txt") as file:
    for line in file:
      names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")