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
        
        user_id=User.add_one(data)
        user_data={
            "id":user_id
        }
        current_user=User.get_one(user_data)
        session["user_id"]=current_user.id
        session["full_name"]=current_user.first_name+ " "+current_user.last_name
        return redirect('/todos')
@app.route("/user/login",methods=["POST"])
def login_processing():
    data={
        "email":request.form["email"]
    }
    current_user=User.get_one_by_email(data)
    if current_user==None:
        return redirect("/")
    else:
        if not (User.validate_password(current_user.password,request.form["password"])):
            return redirect("/")
        else:
            session["user_id"]=current_user.id
            session["full_name"]=current_user.first_name+" "+current_user.last_name
            return redirect("/todos")


