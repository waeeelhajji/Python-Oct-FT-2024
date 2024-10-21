users = [
    {
        "first": "Ada",
        "last": "Lovelace"
        }, # index 0
    {
        "first": "Alan",
        "last": "Turing"
        }, # index 1
    {
        "first": "Eric",
        "last": "Idle"
        } # index 2
]
for i in range(len(users)):
    print(f"the index is {i}, and the data is {users[i]}")
print("#"*40)
for i in range (len(users)):
    print(f"the index is {i} and the last name is {users[i]['last']}")
    
print("#"*40)
for i in range (len(users)):
    print(f"the index is {i}")
    for key in users[i]:
        print(f"the key is {key} and the value is {users[i][key]} ")
        

#lists inside of dictionaries
student={
    "first_name":["Alex","Martha","Roger"],
    "last_name":["Miller","Smith","Anderson"],
    "age":[20,25,40],
    "stacks":["python","mern","csharp"]
}

print("#"*10)
print(student['stacks'][0])
for key in student:
    print("+"*50)
    print(f"the key is {key}")
    print(f"the list is {student[key]}")
    for i in range(len(student[key])):
        print(f"the item inside the list is {student[key][i]}")


    