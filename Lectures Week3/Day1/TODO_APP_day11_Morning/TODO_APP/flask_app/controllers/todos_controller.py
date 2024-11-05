from flask import session,request,render_template,redirect
from flask_app.models.todos_model import Todo
from flask_app import app

@app.route("/todos",methods=["GET"])
def get_todos():
    session["user_name"]="Alex Miller"
    session["user_id"]=12
    
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

@app.route("/todo/delete/<int:id>",methods=["POST"])
def delete_todo(id):
    data={
        "id":id
    }
    Todo.delete_one(data)
    return redirect("/todos")

@app.route("/todo/form/update/<int:id>",methods=["GET"])
def update_form(id):
    data={
        "id":id
    }
    todo=Todo.get_one(data)
    return render_template("update_form.html",todo=todo)
@app.route("/todo/update/<int:id>",methods=["POST"])
def update_todo(id):
    data={
        "id":id,
        "name":request.form["todo_name"],
        "status":request.form["todo_status"]
    }
    Todo.update_one(data)
    return redirect("/todos")
    