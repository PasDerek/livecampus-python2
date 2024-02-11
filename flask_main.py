from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/<string:url>', methods=['POST'])
def update_responses(url):
    data = request.json

    id_formulaire = data.get('id_formulaire')
    username = data.get('username')
    progression = data.get('progression')
    difficulte = data.get('difficulte')
    maitrise = data.get('maitrise')

    print(id_formulaire)
    print(username)
    print(progression)
    print(difficulte)
    print(maitrise)

    return jsonify({'message': 'bla bla bla'})

if __name__ == '__main__':
    app.run(debug=True)