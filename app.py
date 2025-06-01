from flask import Flask, jsonify, render_template


app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'analista de dados',
    'local': 'Nampula',
    'salario': '10000'
},
        
         
 ]

@app.route("/")
def home():
    return  render_template('home.html', vagas=VAGAS)

@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

