# key: value pairs

student_1 = {
    "name": "Susan",
    "stream": "Tech",
    "completed_lessons": 4,
    "completed_lessons_names": ["variables", "data types", "set up"]
}

print(student_1)
print(type(student_1))
print(student_1["stream"]) # prints the value for the key "stream"S
print(student_1["completed_lessons_names"]) # prints the value of this key (list)
student_1["completed_lessons"] = 3 # amends the value for this key from 4 to 3
print(student_1)
print(student_1("completed_lessons_names"[1]))
print(student_1.keys())


