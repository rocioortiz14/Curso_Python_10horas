
### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("INTERMEDIO/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Rocio\nMi apellido es Ochoa\n35 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta PHP")
print(txt_file.readline())

txt_file.close()

with open("INTERMEDIO/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")
# .json file


json_file = open("INTERMEDIO/my_file.json", "w+")

json_test = {
    "name": "Rocio",
    "surname": "Ochoa",
    "age": 35,
    "languages": ["Python", "PHP", "JS"],
    "Facebook": "https://www.facebook.com/rocsibonita14"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("INTERMEDIO/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("INTERMEDIO/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("INTERMEDIO/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Rocio", "Ochoa", 35, "Python",  "https://www.facebook.com/rocsibonita14"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("INTERMEDIO/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file
