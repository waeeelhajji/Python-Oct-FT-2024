from mysqlconnection import connectToMySQL

class Todo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.status=data["status"]
        self.created_at=data["created_at"]
        self.updated_at=data['updated_at']
        self.user_id=data["user_id"]
        
    @classmethod
    def get_all(cls):
        query="SELECT * FROM todos;"
        result=connectToMySQL("todos_db").query_db(query)#should be a list of dictionaries
        # print("@"*100)
        # print(result)
        # print("@"*100)
        list_of_todos=[]
        
        # print(todo1.id)
        for data in result:
            list_of_todos.append(Todo(data))
        # print(list_of_todos)
        return list_of_todos
    
    @classmethod
    def create_one(cls,data):
        query="INSERT INTO todos(name,status,user_id)"
        query +="VALUES (%(name)s,%(status)s,%(user_id)s);"
        result=connectToMySQL("todos_db").query_db(query,data)
        print(result)
            
        