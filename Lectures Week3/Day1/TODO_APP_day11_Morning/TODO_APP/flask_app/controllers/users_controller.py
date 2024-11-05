from flask import session,request,render_template,redirect
from flask_app import app
from flask_app.models.users_model import User


@app.route("/user/get",methods=["GET"])
def get_my_todos():
    
    data={
        "id":session["user_id"]
    }
    current_user=User.get_one_with_todos(data)
    return render_template("user_with_todos.html",current_user=current_user)

@app.route("/",methods=["GET"])
@app.route("/registration",methods=["GET"])
@app.route("/login",methods=["GET"])
def registration():
    return render_template("index.html")

@app.route("/user/new",methods=["POST"])
def create_user():
    data={
        # "first_name":request.form["first_name"],
        # "last_name":request.form["last_name"],
        # "email":request.form["email"],
        # "password":request.form["password"]
        # "password_confirmation":request.form["password_confirmation"]
        **request.form
        
    }
    print(data)
    is_valid=User.validate_data(data)
    if is_valid==False:
        return redirect("/")
    else:
        data["password"]=User.encrypt_string(data["password"])
        
        User.add_one(data)
        
        return redirect('/todos')


