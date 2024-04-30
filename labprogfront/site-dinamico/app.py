from flask import Flask, render_template
from cardapio import Cardapio

app = Flask(__name__)

hamburguer = Cardapio(1, "Hamburguer", "23.00", "imagens/hamburguer.jpeg", "pao")
macarrao = Cardapio(2, "Macarrao", "24.00", "imagens/image.png", "macarrao")
petiscos = Cardapio(3, "Petiscos", "25.00", "imagens/petiscos.jpeg", "carne")
pizza = Cardapio(4, "Pizza", "26.00", "imagens/pizza.jpeg", "calabresa")
cardapio_catalogo = [hamburguer, macarrao, petiscos, pizza]

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/")
def catalogo():
    return render_template ("cardapio.html")

# @app.route("/pizza")
# def pizza():
#     return render_template ("pizza.html")

# @app.route("/macarrao")
# def macarrao():
#     return render_template ("macarrao.html")

# @app.route("/petiscos")
# def petiscos():
#     return render_template ("petiscos.html")

# @app.route("/hamburguer")
# def hamburguer():
#     return render_template ("hamburguer.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html", 
                           cardapios = cardapio_catalogo)

@app.route("/cardapio/<int:id>")
def cardapio(id:int):
    for cardapio_do_catalogo in cardapio_catalogo:
        if cardapio_do_catalogo.id == id:
            return render_template("curso.html", curso = cardapio_do_catalogo)
    return "<h1>Ops! Curso não encontrado!</h1>"