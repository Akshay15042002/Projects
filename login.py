from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials for demonstration
valid_credentials = {
    'admin': 'password123',
    'user': '123456'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in valid_credentials and password == valid_credentials[username]:
        # Successful login
        return redirect(url_for('dashboard'))
    else:
        # Invalid credentials
        error = 'Invalid username or password. Please try again.'
        return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    # Display the dashboard after successful login
    return 'Welcome to the Dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
