#list in python are arrays in js
students=["Alex","Martha","Roger","Julie"]
print(students[1])
students[3]="Juliette"
print(students[3])
#pop, append
students.append("Micheal")
print(students)

students.pop(-1)
print(students)
print(len(students))

# tuples: immutable lists
alex=("Alex","Miller",20)
print(type(alex))
first_name=alex[0]
print(first_name)

