HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>6F IT Solutions</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;
}

body{

height:100vh;
overflow:hidden;
display:flex;
justify-content:center;
align-items:center;

background:linear-gradient(135deg,#0F2027,#203A43,#2C5364,#1C92D2);
background-size:400% 400%;
animation:bg 12s ease infinite;

}

@keyframes bg{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}

.circle{

position:absolute;
border-radius:50%;
background:rgba(255,255,255,.08);
animation:float 12s linear infinite;

}

.circle:nth-child(1){

width:250px;
height:250px;
top:-60px;
left:-60px;

}

.circle:nth-child(2){

width:180px;
height:180px;
bottom:40px;
right:100px;

}

.circle:nth-child(3){

width:120px;
height:120px;
top:150px;
right:-40px;

}

@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(30px);
}

100%{
transform:translateY(0px);
}

}

.container{

width:900px;
display:flex;
align-items:center;
justify-content:space-between;

padding:50px;

border-radius:25px;

background:rgba(255,255,255,.12);

backdrop-filter:blur(18px);

box-shadow:0 15px 40px rgba(0,0,0,.4);

color:white;

z-index:2;

}

.left{

width:55%;

}

.logo{

width:120px;
height:120px;

border-radius:50%;

background:white;

display:flex;
align-items:center;
justify-content:center;

font-size:45px;
font-weight:bold;

color:#1C92D2;

margin-bottom:30px;

box-shadow:0 0 30px rgba(255,255,255,.4);

}

h1{

font-size:48px;
font-weight:700;

margin-bottom:15px;

}

h2{

font-size:26px;
font-weight:500;

color:#FFD54F;

margin-bottom:25px;

}

p{

font-size:18px;

line-height:32px;

color:#EAEAEA;

}

.version{

margin-top:30px;

display:inline-block;

padding:10px 22px;

background:#FFD54F;

color:#222;

border-radius:30px;

font-weight:bold;

}

.right{

width:35%;
text-align:center;

}

.right img{

width:280px;

animation:move 4s ease infinite;

}

@keyframes move{

0%{
transform:translateY(0);
}

50%{
transform:translateY(-15px);
}

100%{
transform:translateY(0);
}

}

.buttons{

margin-top:35px;

display:flex;

gap:15px;

flex-wrap:wrap;

}

.btn{

padding:14px 28px;

border:none;

border-radius:50px;

cursor:pointer;

font-size:16px;

font-weight:600;

transition:.3s;

}

.btn-primary{

background:#FFD54F;

color:#222;

}

.btn-primary:hover{

transform:translateY(-4px);

box-shadow:0 8px 20px rgba(255,213,79,.5);

}

.btn-secondary{

background:transparent;

border:2px solid white;

color:white;

}

.btn-secondary:hover{

background:white;

color:#1C92D2;

}

@media(max-width:850px){

.container{

width:95%;
flex-direction:column;
text-align:center;

}

.left,.right{

width:100%;

}

.logo{

margin:auto;
margin-bottom:25px;

}

.buttons{

justify-content:center;

}

.right img{

margin-top:30px;
width:220px;

}

}

</style>

</head>

<body>

<div class="circle"></div>
<div class="circle"></div>
<div class="circle"></div>

<div class="container">

<div class="left">

<div class="logo">6F</div>

<h1>WELCOME TO 6F IT</h1>

<h2>Every Person Deserves a Great Career</h2>

<p>

Build Your Future.<br>

Learn • Practice • Grow • Succeed.<br>

Create. Innovate. Transform.

</p>

<div class="version">

Version : {{ version }}

</div>

<div class="buttons">

<button class="btn btn-primary">Get Started</button>

<button class="btn btn-secondary">Learn More</button>

</div>

</div>

<div class="right">

<img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png">

</div>

</div>

</body>

</html>
"""
