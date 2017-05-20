# N'oubliez pas d'importer request
from flask import Flask, render_template, request

app = Flask("Forms and Request")

@app.route("/")
def form():
    # servons un formulaire à la racine
    return render_template("form.html")

# l'action du formulaire doit mener à /resultat avec la méthode POST et il faut
# indiquer cette méthode dans @app.route() (par défaut seule la méthode GET est
# prise en charge).
@app.route("/resultat", methods=['POST'])
def resultat():
    # l'objet request contient un attribut form qui est un dictionnaire des
    # noms du formulaire vers les valeurs associées
    return "L'utilisateur " + request.form['username'] + " a écrit le texte : " + request.form['texteComplet']

app.run(debug=True)