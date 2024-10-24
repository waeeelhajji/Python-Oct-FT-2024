from flask import Flask, render_template #Import Flask to to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"


@app.route('/') # Using a decorator to listen for endpoints
# the @ decorator associates this route with the function immediately following
def hello():
    print("server is running !!!!!!!!!!!!!")
    return "Hello Flask !"

# Rendering Templates
@app.route('/html')
def first_html():
    # Render a template
    return render_template('index.html')

# 
@app.route('/loop')
def loop():
    # Looping with Jinja and displaying information
    fruits=['Apple','Orange','Pear','Banana']
    # Passing data from server to template
    return render_template('loop.html', items=fruits)

# Setting up routes to accept path variables
@app.route('/hello/<user_name>/<int:number>')
def hello_user(user_name,number):
    return render_template('many_names.html', user_name=user_name, number=number)


if __name__=="__main__": # Ensure this file is being run directly
    app.run(debug=True) # Run the app in debug mode