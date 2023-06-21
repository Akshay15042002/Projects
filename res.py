from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Generate OTP
def generate_otp():
    digits = '0123456789'
    otp_length = 6
    otp = ''
    for _ in range(otp_length):
        otp += random.choice(digits)
    return otp

# Routes
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        
        # Send OTP to the phone number (You can use an SMS gateway or any other method)

        otp = generate_otp()
        # Store the OTP in session or database for verification
        # For simplicity, we will store it in session here
        session['otp'] = otp
        session['name'] = name
        session['email'] = email
        session['password'] = password
        session['phone'] = phone

        return redirect(url_for('verify'))

    return render_template('registration.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        stored_otp = session.get('otp')

        if user_otp == stored_otp:
            # OTP verification successful
            name = session.get('name')
            email = session.get('email')
            password = session.get('password')
            phone = session.get('phone')

            # Perform further actions like saving the user to the database

            # Clear the session variables
            session.pop('otp', None)
            session.pop('name', None)
            session.pop('email', None)
            session.pop('password', None)
            session.pop('phone', None)

            return render_template('success.html', name=name)
        else:
            # Invalid OTP
            return render_template('verification.html', error='Invalid OTP! Please try again.')

    return render_template('verification.html')

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
