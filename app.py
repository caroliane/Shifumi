from flask import Flask, render_template, jsonify, request
from random import randint

app = Flask(__name__)

# Liste des options
jeu = ["pierre", "papier", "ciseaux"]

# Initialiser des points pour le joueur et l'ordinateur
Pointsjoueur = 0
Pointsordinateur = 0

# Initialiser la variable continuer en dehors de la route principale
continuer = True

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Gestion de la requête AJAX depuis la page web
@app.route('/play', methods=['POST'])
def play():
    global continuer, Pointsjoueur, Pointsordinateur

    # Récupérer le choix deu joueur depuis la requête
    joueur = request.form.get('choice')

    # Attribuer une option aléatoire à l'ordinateur
    ordinateur = jeu[randint(0, 2)]

    # Vérification des scénarios
    result = determine_winner(joueur, ordinateur)

    # Mise à jour des points
    if result == "Gagné !":
        Pointsjoueur += 1
    elif result == "Perdu !":
        Pointsordinateur += 1

    # Retourner le résultat au format JSON
    return jsonify({
        'result': result,
        'Pointsjoueur': Pointsjoueur,
        'Pointsordinateur': Pointsordinateur,
        'ordinateur': ordinateur
    })

def determine_winner(joueur, ordinateur):
    # Logique pour déterminer le résultat du jeu
    if joueur == ordinateur:
        return "Egalité!"
    elif joueur == "pierre":
        if ordinateur == "papier":
            return "Perdu !"
        else:
            return "Gagné !"
    # elif joueur == "pierre":
    #     if ordinateur == "ciseaux":
    #         return "Gagné !"
        # else:
        #     return "Perdu !"
    elif joueur == "papier":
        if ordinateur == "ciseaux":
            return "Perdu !"
        else:
            return "Gagné !"
    elif joueur == "ciseaux":
        if ordinateur == "pierre":
            return "Perdu !"
        else:
            return "Gagné !"
    else:
        return "Votre choix n'est pas correct, vérifiez l'orthographe!"

if __name__ == '__main__':
    app.run(debug=True)





