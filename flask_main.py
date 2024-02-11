from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
import sys
sys.path.append('mon_projet')
from mon_projet import env

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = env.SECRETS["FLASK"]

@app.route('/', methods=['POST'])
@cross_origin()
def update_responses():
    data = request.json
    print(data)

    # id_formulaire = data.get('id_formulaire')
    # username = data.get('username')
    # progression = data.get('progression')
    # difficulte = data.get('difficulte')
    # maitrise = data.get('maitrise')

    return jsonify({'message': 'bla bla bla'})

if __name__ == '__main__':
    app.run(debug=True)