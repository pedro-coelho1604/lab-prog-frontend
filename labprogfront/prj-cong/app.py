from flask import Flask, render_template
from palestrante import Sessao, Palestrante

app = Flask(__name__)

joao = Palestrante(1, "Gosto de animais", "nutricao", "Dieta", "Foi meu professor na faculdade", "Gostei")
pedro = Palestrante(2, "Gosto de livros", "medicina", "Cancer", "Sabe muito", "Nao gostei")
gabriel = Palestrante(3, "Gosta de saude", "neuromedicina", "estresse", "Muito inteligente", "Adorei")
catalogo_palestrantes = [joao, pedro, gabriel]

comida = Sessao(1, "Falando sobre os carboidratos", "10h", "Palco 1", "Muito interessante")
sangue = Sessao(2, "Falando sobre as moleculas do sangue", "12h", "Palco 2", "Muito útil para atletas")
sono = Sessao(3, "Falando sobre qualidade do sono", "14h", "Palco 3", "Estava precisando escutar sobre isso")
catalogo_sessoes = [comida, sangue, sono]

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
        if catalogo_de_sessoes.id == id:
            return render_template("sessoes.html", sessao = catalogo_de_sessoes)
    return "<h1>Ops! Sessão não encontrado!</h1>"


if __name == '__main__':
    app.run(debug=true)