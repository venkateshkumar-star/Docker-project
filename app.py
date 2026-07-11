from flask import Flask, render_template_string, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "users.db"


# ---------------- DATABASE ---------------- #

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- HTML ---------------- #

HTML = """

<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>6F IT</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial;
}

body{

height:100vh;
display:flex;
justify-content:center;
align-items:center;

background:linear-gradient(-45deg,#0f2027,#203a43,#2c5364,#1c92d2);
background-size:400% 400%;
animation:bg 10s ease infinite;

}

@keyframes bg{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}

.container{

width:800px;
display:flex;
background:rgba(255,255,255,.12);
backdrop-filter:blur(10px);
border-radius:20px;
overflow:hidden;
box-shadow:0 15px 40px rgba(0,0,0,.4);

}

.left{

width:50%;
padding:40px;
color:white;
text-align:center;

}

.logo{

width:100px;
height:100px;
border-radius:50%;
background:white;
color:#1c92d2;
font-size:40px;
font-weight:bold;

display:flex;
justify-content:center;
align-items:center;

margin:auto;
margin-bottom:25px;

}

.left h1{

font-size:40px;
margin-bottom:20px;

}

.left h2{

color:#FFD54F;
margin-bottom:20px;

}

.left p{

font-size:18px;
line-height:30px;

}

.right{

width:50%;
background:white;
padding:40px;

}

form{

display:none;

}

form.active{

display:block;

}

h3{

text-align:center;
margin-bottom:20px;
color:#1c92d2;

}

input{

width:100%;
padding:12px;
margin:10px 0;
border-radius:8px;
border:1px solid #ccc;
font-size:16px;

}

button{

width:100%;
padding:12px;
margin-top:10px;

background:#1c92d2;
color:white;

border:none;
border-radius:8px;
cursor:pointer;

font-size:16px;

}

button:hover{

background:#0f7ec7;

}

.links{

text-align:center;
margin-top:20px;

}

.links a{

display:block;
margin:8px;
cursor:pointer;
color:#1c92d2;
text-decoration:none;

}

.flash{

background:#ffeeba;
padding:10px;
margin-bottom:15px;
border-radius:8px;
text-align:center;

}

.success{

background:#d4edda;

}

</style>

</head>

<body>

<div class="container">

<div class="left">

<div class="logo">6F</div>

<h1>WELCOME</h1>

<h2>Every Person Deserves a Great Career</h2>

<p>

Build Your Future<br>
Learn • Practice • Grow • Succeed

</p>

</div>


<div class="right">

{% with messages = get_flashed_messages() %}
{% if messages %}
{% for msg in messages %}
<div class="flash">{{msg}}</div>
{% endfor %}
{% endif %}
{% endwith %}

<!-- LOGIN -->

<form method="POST" action="/login" id="login" class="active">

<h3>Login</h3>

<input type="text" name="username" placeholder="Username" required>

<input type="password" name="password" placeholder="Password" required>

<button>Login</button>

<div class="links">

<a onclick="show('signup')">Create Account</a>

<a onclick="show('forgot')">Forgot Password?</a>

</div>

</form>


<!-- SIGNUP -->

<form method="POST" action="/signup" id="signup">

<h3>Sign Up</h3>

<input type="text" name="username" placeholder="Username" required>

<input type="password" name="password" placeholder="Password" required>

<button>Create Account</button>

<div class="links">

<a onclick="show('login')">Back to Login</a>

</div>

</form>


<!-- FORGOT -->

<form method="POST" action="/forgot" id="forgot">

<h3>Forgot Password</h3>

<input type="text" name="username" placeholder="Username" required>

<input type="password" name="newpassword" placeholder="New Password" required>

<button>Reset Password</button>

<div class="links">

<a onclick="show('login')">Back to Login</a>

</div>

</form>

</div>

</div>


<script>

function show(id){

document.querySelectorAll("form").forEach(f=>f.classList.remove("active"));

document.getElementById(id).classList.add("active");

}

</script>

</body>
</html>

"""


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template_string(HTML)


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()

    conn.close()

    if row and check_password_hash(row[0], password):

        session["user"] = username
        flash("Login Successful!")

    else:

        flash("Invalid Username or Password")

    return redirect("/")


# ---------------- SIGNUP ---------------- #

@app.route("/signup", methods=["POST"])
def signup():

    username = request.form["username"]
    password = generate_password_hash(request.form["password"])

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    try:

        c.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()

        flash("Account Created Successfully!")

    except:

        flash("Username Already Exists")

    conn.close()

    return redirect("/")


# ---------------- FORGOT PASSWORD ---------------- #

@app.route("/forgot", methods=["POST"])
def forgot():

    username = request.form["username"]
    newpass = generate_password_hash(request.form["newpassword"])

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    row = c.fetchone()

    if row:

        c.execute(
            "UPDATE users SET password=? WHERE username=?",
            (newpass, username)
        )

        conn.commit()

        flash("Password Updated Successfully!")

    else:

        flash("Username Not Found")

    conn.close()

    return redirect("/")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged Out")

    return redirect("/")


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
