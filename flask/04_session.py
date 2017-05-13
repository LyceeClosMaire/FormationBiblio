# N'oubliez pas d'importer session en plus de request et Flask
from flask import Flask, session, request, redirect

app = Flask("Sessions")

@app.route('/')
def index():
    # vérifions si session contient la clé 'username' et si oui affichons un message
    # spécifique
    if 'username' in session:
        return 'Connecté comme ' + session['username']
    else:
        return "Vous n'êtes pas encore connecté."

# voici un exemple de route acceptant les deux méthodes GET et POST
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    # si la méthode était POST, on a été appelé par un formulaire,
    # la variable request contient les données de ce formulaire
    if request.method == 'POST':
        # on place le contenu du champ 'username' du formulaire dans
        # le dictionnaire session, pour le conserver
        session['username'] = request.form['username']
        # puis on redirige le client vers la route / qui correspond à la fonction index()
        return redirect('/')

    # sinon la méthode est GET et on affiche le formulaire de connection
    else:
        return '''
            <form method="post" action="/connexion">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

@app.route('/deconnexion')
def deconnexion():
    # on supprime la clé 'username' du dictionnaire session si elle y est présente
    session.pop('username', None)
    # puis on redirige le visiteur vers la racine.
    return redirect('/')

# session utilise de la cryptographie pour assurer le secret et l'inviolabilité des
# données du côté client, donc vous devez régler une clé secrète pour votre application
# (et elle doit rester identique pour que les sessions restent lisibles)
# Utilisez un résultat du code : "import os; os.urandom(24)" pour avoir une bonne clé
app.secret_key = b'\xecG\x0b\x14\x9a\\H\xd0\xb5\x07v\x96\x86\x93\xaf\x10\xe7\xed\xcbdm\xef\xa4\xfe'

app.run(debug=True)