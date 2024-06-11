from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)

# Set this to true to randomize a pin
random_pin = False

# Define specific pin
secret_pin = 111222

# Generate a random pin if randomizer enabled
if random_pin:
    secret_pin = random.randint(100000, 999999)

LOGIN_SITE = 'login.html'
DESIRED_SITE = 'mywebsite.html'


@app.route('/', methods=['GET', 'POST'])
def show_login_page():
    # Check if the method of requesting to the server is POST 
    # aka the HTML secure form method
    if request.method == 'POST':
        # Retrieve the code from the form within the HTML
        entered_pin = request.form['code']
        # Check if the pins match
        if int(entered_pin) == secret_pin:
            # If the PIN is correct, set a session variable to mark the user as logged in
            session['logged_in'] = True
            return redirect(url_for('mywebsite'))
        else:
            return "Incorrect pin"
    return render_template(LOGIN_SITE)


@app.route('/mywebsite')
def mywebsite():
    # Check if the user is logged in
    if not session.get('logged_in'):
        # If not logged in, redirect to the login page
        return redirect(url_for('show_login_page'))
    # If logged in, render the website
    return render_template(DESIRED_SITE)


if __name__ == "__main__":
    # Set a secret key for the session
    app.secret_key = 'kjZD-gfT8-2435-jKdf-80Q5-tj2GK'
    app.run(host="0.0.0.0", port=5000)
