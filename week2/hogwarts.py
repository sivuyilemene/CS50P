# LISTS
# list_name = [value]
students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])
    
# DICTS
# dict_name = {key:value}
students_dict = {
      "Hermoine":"Gryffindor",
      "Harry":"Gryffindor",
      "Ron":"Gryffindor",
      "Draco": "Slytherin",
}

print(students_dict["Hermoine"])
print(students_dict["Harry"])
print(students_dict["Ron"])
print(students_dict["Draco"])

for student in students_dict:
    print(student, students_dict[student], sep=", ")
    
school = [
    {"name":"Hermoine", "house":"Gryffindor", "petronus":"otter"},
    {"name":"Harry", "house":"Gryffindor", "petronus":"stag"},
    {"name":"Ron", "house":"Gryffindor", "petronus":"jack russell terrier"},
    {"name":"Draco", "house":"Slytherin", "petronus":None},
]

for s in school:
    print(s["name"], s["house"], s["petronus"], sep=", ")