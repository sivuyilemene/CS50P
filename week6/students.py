# read a csv file
# with open("students.csv") as file:
#   for line in file:
#       name,house = line.rstrip().split(",")
#       print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#   for line in file:
#       name,house = line.rstrip().split(",",maxsplit=1)
#       student = {"name":name, "house":house}
#       # student["name"] = name
#       # student["house"] = house
#       students.append(student)
      
# def get_name(student):
#   return student["name"]

# # print(students)  
# for person in sorted(students, key=lambda student: student["name"]):
#     print(f"{person['name']} is in {person['house']}")


import csv

# students = []

# with open("students.csv") as file:
#   reader = csv.reader(file)
#   # for row in reader:
#   #   students.append({"name": row[0], "house":row[1]})
#   for name,house in reader:
#     students.append({"name": name, "house":house})
  
# for person in sorted(students, key=lambda student: student["name"]):
#     print(f"{person['name']} is in {person['house']}")



# students = []

# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   # for row in reader:
#   #   students.append({"name": row[0], "house":row[1]})
#   for row in reader:
#     students.append({"name": row["name"], "house":row["house"]})
  
# for person in sorted(students, key=lambda student: student["name"]):
#     print(f"{person['name']} is in {person['house']}")


# Writee to csv

name = input("whats your name? ")
house = input("Whats your house? ")

with open("students.csv","a") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "house"])
  writer.writerow({"name":name, "house":house})