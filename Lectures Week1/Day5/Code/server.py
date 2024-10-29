from flask import Flask, render_template, request, redirect, session # type: ignore
app = Flask(__name__)
app.secret_key = 'supersecretkey' # Needed to use sessions

# Index route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle POST request (submit message)
@app.route('/submit2', methods=['POST'])
def submit():
    # Display the form data
    print(request.form)

    # Extracting the form data from the post request
    message = request.form['message']
    user = request.form['user_name']

    # Save our data to session
    session['message'] = message
    session['user'] = user
    # return redirect('/result')
    ############################################

    # make sure that our key exist in session
    if 'messages' not in session:
        session['messages'] = []
    # add the new message to the list 
    messages = session['messages']
    messages.append(message)
    session['messages'] = messages
    ##### redirect after a POST request #####
    return redirect('/')

# Show the result on another page
@app.route('/result')
def result():
    return render_template('result.html')

# route to clear the session
@app.route('/clear')
def clear():
    session.clear() # clear session data
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)