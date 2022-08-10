from flask import Flask, render_template

app = Flask("hello")
nomeAula = " Aula de Python para Web"

@app.route("/")
def hello():
    return "Hello World"

@app.route("/usuario")
def usuario():  
    usurario = [1, "Daniele Miron", "Professor"]  
    return render_template("index.html", usuario=usuario)

@app.route("/contatos")
def contato():
    return render_template("index.html", usuario=usuario)