from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/input")
def display_user_input():

    return render_template('signup_form.html', username_error='', password_error='', verify_password_error='',
      email_error='', username='', password='', verify_password='', email='')

@app.route("/input", methods=['POST'])
def validate_input():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == "":
        username_error = "Invalid Username"
    if password == "":
        password_error = "Invalid Password"
    if verify_password == "":
        verify_password_error = "Invaild Password"

    if password != verify_password:
        verify_password_error = "Passwords Do Not Match"
        
    
    if len(username) > 20 or len(username) < 3:
        username_error = "Invalid Username"
    if len(password) > 20 or len(password) < 3:
        password_error = "Invalid Password"
        

    if ' ' in username:
        username_error = "Invaild Username"
    if ' ' in password:
        password_error = "Invaild Password"
    if ' ' in verify_password:
        verify_password_error = "Invalid Password"
        

    if email != "":
        if len(email) > 20 or len(email) < 3:
            email_error = "Invaild Email"
        if '@' and '.' not in email:
            email_error = "Invalid Email"
        if ' ' in email:
            email_error = "Invalid Email" 
        if email.count('@') > 1:
            email_error = "Invalid Email"
        if email.count('.') > 1:
            email_error = "Invalid Email"
        

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('signup_form.html', username_error=username_error, username=username, password_error=password_error, 
        verify_password_error=verify_password_error, email_error=email_error, password='', verify_password='', email=email)
  
@app.route('/welcome')
def hello(): 
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()       