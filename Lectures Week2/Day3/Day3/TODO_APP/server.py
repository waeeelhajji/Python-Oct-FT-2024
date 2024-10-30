from flask import Flask, render_template,redirect,request,session
from todos_model import Todo

app=Flask(__name__)
app.secret_key="password123"

list_of_todos=[
    {
        "id":1,
        "name":"Learning flask",
        "status":"pending"
    },
    {
        "id":2,
        "name":"Learning SQL",
        "status":"in progress"
    },
    {
        "id":3,
        "name":"Learning ERD",
        "status":"completed"
    },
    {
        "id":4,
        "name":"Learning OOP",
        "status":"not yet started"
    }
]

@app.route("/todos",methods=["GET"])
def get_todos():
    session["user_name"]="Alex Miller"
    session["user_id"]=1
    
    list_of_todos1=Todo.get_all()
    
    return render_template("todos.html",list_of_todos=list_of_todos1)

@app.route("/todo/form",methods=["GET"])
def display_todo_form():
    return render_template("todo_form.html")
@app.route("/todo/new",methods=["POST"])
def create_todo():
    new_todo={

        "name":request.form["todo_name"],
        "status":request.form["todo_status"],
        "user_id":session["user_id"]
    }
    result=Todo.create_one(new_todo)
    # list_of_todos.append(new_todo)
    return redirect("/todos")

if __name__ == "__main__":
    app.run( debug = True, port = 5001 )
