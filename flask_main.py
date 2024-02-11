from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
import sys
sys.path.append('mon_projet')
from mon_projet import env, settings


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = env.SECRETS["FLASK"]

mydb = mysql.connector.connect(
    host="localhost",
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    database=settings.DATABASES['default']['NAME']
)


@app.route('/', methods=['POST'])
@cross_origin()
def update_responses():
    data = request.json
    id_formulaire = data.get('id_formulaire')
    numero_etudiant = data.get('numero_etudiant')
    progression = data.get('progression')
    difficulte = data.get('difficulte')
    maitrise = data.get('maitrise')

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * from mon_projet_reponsesformulaire WHERE id_formulaire_id = {id_formulaire} AND numero_etudiant_id = {numero_etudiant};")
    if mycursor.fetchall():
        mycursor.execute(f"UPDATE mon_projet_reponsesformulaire SET progression = {progression}, difficulte = \"{difficulte}\", maitrise = \"{maitrise}\" WHERE id_formulaire_id = {id_formulaire} AND numero_etudiant_id = {numero_etudiant};")
        mydb.commit()
    else:
        mycursor.execute(f"INSERT INTO mon_projet_reponsesformulaire (progression, difficulte, maitrise) VALUES ({progression}, \"{difficulte}\",  \"{maitrise}\");")
        mydb.commit()


    return jsonify({'message': 'bla bla bla'})

if __name__ == '__main__':
    app.run(debug=True)