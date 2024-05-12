from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/process-url', methods=['POST'])
def process_url():
    data = request.get_json()
    url = data['url']
    
    # Exécutez le script Python check.py avec l'URL comme argument
    result = subprocess.check_output(['python', 'check.py', url], universal_newlines=True)
    
    # Traitez le résultat si nécessaire
    # ...

    # Retournez une réponse JSON
    response = {'message': 'URL traitée avec succès', 'result': result}
    return jsonify(response)

if __name__ == '__main__':
    app.run()