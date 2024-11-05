from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE,app
from flask_app.models.todos_model import Todo
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt=Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.list_of_todos=[]
    
    @classmethod
    def get_one_with_todos(cls,data):
        query="select * from users u left join todos t on t.user_id =u.id where u.id=%(id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        print("8"*100)
        print(result)
        print("8"*100)
        current_user=User(result[0])
        print(current_user.first_name)
        for row in result:
            todo_data={
                "id":row["t.id"],
                "name":row["name"],
                "status":row["status"],
                "created_at":row["t.created_at"],
                "updated_at":row["t.updated_at"],
                "user_id":row["user_id"]
            }
            new_todo=Todo(todo_data)
            current_user.list_of_todos.append(new_todo)
        return current_user
    
    @classmethod
    def add_one(cls,data):
        query="insert into users(first_name,last_name,email,password) values(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @staticmethod
    def encrypt_string(text):
        encrypted_string=bcrypt.generate_password_hash(text)
        print(encrypted_string)
        return encrypted_string
    
    @staticmethod
    def validate_data(data):
        first_name=data["first_name"]
        last_name=data["last_name"]
        email=data["email"]
        is_valid=True
        if len(first_name)<3:
            is_valid=False
            flash("First Name needs to have at least 3 characters","first_name_validation")
        if len(last_name)<3:
            is_valid=False
            flash("Last Name needs to be at least 3 characters","last_name_validation")
        if not EMAIL_REGEX.match(email): 
            flash("Invalid email address!","email_validation")
            is_valid = False
        return is_valid
