#Dictionaries are objects in JS. we can access dictionairies with []
student={
    "first_name":"Alex",
    "last_name":"Miller",
    "age":20
}
print(student)
print(f'my name is {student["first_name"]}')
student["python_exam_score"]=8.4
print(student)
student.pop("first_name")
print(student)