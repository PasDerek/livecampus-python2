from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
import sys
sys.path.append('mon_projet')
from mon_projet import env, settings

# Initialisation : app flask et cors
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = env.SECRETS["FLASK"]

# Création du connecteur avec la base de donnée
mydb = mysql.connector.connect(
    host=settings.DATABASES['default']['HOST'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    database=settings.DATABASES['default']['NAME']
)

# Route par défaut recevant les données fourni par la fonction 'collecterDonneesEtEnvoyer()' de 'etudiant_formulaire.html'
@app.route('/', methods=['POST'])
@cross_origin()
def update_responses():
    # Récupérer les données JSON
    data = request.json
    # Enregistrement des variables
    id_formulaire = data.get('id_formulaire')
    numero_etudiant = data.get('numero_etudiant')
    progression = data.get('progression')
    difficulte = data.get('difficulte')
    maitrise = data.get('maitrise')

    # Récupération des entrées de la table 'reponsesformulaire' pour le formulaire (id_formulaire) et l'étudiant associé (numero_etudiant)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * from mon_projet_reponsesformulaire WHERE id_formulaire_id = {id_formulaire} AND numero_etudiant_id = {numero_etudiant};")
    # Si une entrée existe, mettre à jour les données présente : progression, difficulté, maitrisie
    if mycursor.fetchall():
        mycursor.execute(f"UPDATE mon_projet_reponsesformulaire SET progression = {progression}, difficulte = \"{difficulte}\", maitrise = \"{maitrise}\" WHERE id_formulaire_id = {id_formulaire} AND numero_etudiant_id = {numero_etudiant};")
        mydb.commit()
        mycursor.close()
    # Si l'entrée n'existe pas, créer l'entrée complète : id formulaire, numéro étudiant, progression, difficulté, maitrisie
    else:
        mycursor.execute(f"INSERT INTO mon_projet_reponsesformulaire (id_formulaire_id, numero_etudiant_id, progression, difficulte, maitrise) VALUES ({id_formulaire}, {numero_etudiant}, {progression}, \"{difficulte}\",  \"{maitrise}\");")
        mydb.commit()
        mycursor.close()

    return jsonify({'message': 'bla bla bla'})

if __name__ == '__main__':
    app.run(debug=True)