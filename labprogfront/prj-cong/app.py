from flask import Flask, render_template
from cardapio import Cardapio

app = Flask(__name__)

joao = Palestrante(1)
pedro = Palestrante(2)
gabriel = Palestrante(3)
catalogo_palestrantes = [joao, pedro, gabriel]

ia = Sessao(1)
cloud = Sessao(2)
java = Sessao(3)
catalogo_sessoes = [ia, cloud, java]

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/palestrante")
def palestrante():
    return render_template("palestrante.html", 
                           palestrantes = catalogo_palestrantes)

@app.route("/palestrante/<int:id>")
def palestrante(id:int):
    for catalogo_de_palestrantes in catalogo_palestrantes:
        if catalogo_de_palestrantes.id == id:
            return render_template("palestrante.html", palestrante = catalogo_de_palestrantes)
    return "<h1>Ops! Palestrante não encontrado!</h1>"


@app.route("/sessoes")
def sessoes():
    return render_template("sessoes.html", 
                           sessoes = catalogo_sessoes)

@app.route("/sessoes/<int:id>")
def sessoes(id:int):
    for catalogo_de_sessoes in catalogo_sessoes:
        if catalogo_de_palestrantes.id == id:
            return render_template("palestrante.html", palestrante = catalogo_de_palestrantes)
    return "<h1>Ops! Palestrante não encontrado!</h1>"