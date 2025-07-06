from flask import Flask, render_template,jsonify



app = Flask(__name__)

VAGAS = [

    {'id': 1, 'nome': 'celular', 'codigo': '4565655', 'preco': '20150mt', 'marca': 'nike'},
    {'id': 2, 'nome': 'Desktop', 'codigo': '4565655', 'preco': '22250mt', 'marca': 'Solo'},
    {'id': 3, 'nome': 'Leptop', 'codigo': '4565655', 'preco': '45050mt', 'marca': 'nike'},
    {'id': 4, 'nome': 'Monitor', 'codigo': '4565655', 'preco': '5550mt', 'marca': 'adidas'}

    
]

@app.route("/")
def home():
    return render_template("home.html",vagas=VAGAS)

@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)




if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

