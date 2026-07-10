from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>6F IT</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, Helvetica, sans-serif;
}

body{

    height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    background: linear-gradient(-45deg,#0f2027,#203a43,#2c5364,#1c92d2);
    background-size:400% 400%;

    animation:gradient 12s ease infinite;

    overflow:hidden;

}

@keyframes gradient{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}

.container{

    width:700px;

    text-align:center;

    background:rgba(255,255,255,0.12);

    backdrop-filter:blur(12px);

    border-radius:20px;

    padding:60px;

    color:white;

    box-shadow:0px 15px 40px rgba(0,0,0,0.35);

}

.logo{

    width:120px;
    height:120px;

    margin:auto;

    border-radius:50%;

    background:white;

    color:#1c92d2;

    display:flex;

    justify-content:center;

    align-items:center;

    font-size:48px;

    font-weight:bold;

    margin-bottom:30px;

}

h1{

    font-size:48px;

    letter-spacing:2px;

    margin-bottom:20px;

}

h2{

    font-size:28px;

    color:#FFD54F;

    margin-bottom:20px;

}

p{

    font-size:20px;

    line-height:35px;

    color:#f4f4f4;

}

.footer{

    margin-top:40px;

    font-size:16px;

    color:#dddddd;

}

</style>

</head>

<body>

<div class="container">

<div class="logo">
6F
</div>

<h1>WELCOME TO 6F IT</h1>

<h2>Every Person Deserves a Great Career</h2>

<p>
Build Your Future.<br>
Learn • Practice • Grow • Succeed
</p>

<div class="footer">
Powered by Docker | Jenkins | AWS | DevOps
</div>

</div>

</body>

</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
