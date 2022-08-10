from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contato():
    return """<html> 
    <head> 
        <title> Aula HTML </title>
    </head>
    <body>
        <h1> Daniele Miron </h1>
        <h2> daniele@miron </h2>
        <h3> (11) 9 9999-0000 </h3>
    </body>
    </html>"""


