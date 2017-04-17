# N'oubliez pas d'importer render_template
from flask import Flask, render_template
from random import randint
app = Flask("Templates")

@app.route("/")
def hello():
    # usage de base
    return render_template("helloworld.html")

@app.route("/test")
def test():
    # on peut passer n'importe quelles valeurs au template de façon à ce qu'il puisse
    # les afficher et les explorer. Le nom dans le programme Python n'importe pas,
    # seulement le nom du paramètre dans l'appel à render_template()
    var = "truc"
    return render_template("test.html", liste=[1,2,3], machin=var)

# Mais l'usage classique consiste à construire des valeurs à partir du chemin ou
# de vos fonctions Python et de les passer sous le même nom au template
@app.route("/passage/<name>/<int:num>")
def passage(name, num):
    loops = randint(1,4)
    return render_template("passage.html", name=name, num=num, loops=loops)

app.run(debug=True)