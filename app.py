from flask import Flask, render_template_string
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>6F IT</title>

<style>
/* Your existing CSS */

.version{
    margin-top:30px;
    font-size:18px;
    color:#FFD54F;
    font-weight:bold;
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

    <div class="version">
        Application Version: {{ version }}
    </div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, version=APP_VERSION)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
