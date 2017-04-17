from flask import Flask
# vous créez un objet Flask, qui contiendra tout le nécessaire pour répondre
# aux requêtes
app = Flask("Ceci doit être le nom de votre application")

# ici vous avez le coeur de Flask :
# le @app.route(...) devant une définition de fonction affecte cette fonction
# au chemin indiqué (ici la racine de votre site) de façon à ce que cette fonction
# soit appelée si un client demande ce chemin et le retour de votre fonction est renvoyé
# au client en question
@app.route("/")
def hello():
    return "Hello World!"

# il est possible d'indiquer que certaine partie du chemin sont dynamique,
# autrement dit ces parties peuvent prendre différentes valeurs selon la
# requête exacte du client. Les valeurs exactes sont transmises en argument
# à la fonction. On indique une partie dynamique en l'entourant de <>
@app.route("/<username>")
def goodbye(username):
    return "Goodbye " + username

# souvent vous souhaiteriez qu'une partie dynamique soit d'une certaine forme
# ceci peut être fait en rajoutant un "converter" avant : dans vos <>
# ici "identifier" doit être un entier pour que le chemin soit trouvé par Flask
# et le paramètre identifier de la fonction est un entier
@app.route("/no/<int:identifier>")
def queue(identifier):
    return "Are you really subject n°" + str(identifier) + " ?"

# il est possible d'enchaîner plusieurs parties dynamiques et les convertisseurs
# disponibles qui nous intéressent sont int, float et any :
@app.route("/<any(exp,puissance):name>/<float:num1>/<float:num2>")
def exponentiation(name, num1, num2):
    if name == "exp":
        return str(num1 ** num2)
    elif name == "puissance":
        return "{} puissance {} fait {:.2f}".format(num1, num2, num1**num2)

# lancez le serveur (par défaut sur le port 5000 de l'actuelle machine donc
# accessible comme http://localhost:5000) ici configuré pour donner des informations
# de débogage (à ne jamais faire en production bien sûr !)
app.run(debug=True)