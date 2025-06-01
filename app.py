from flask import Flask, jsonify, render_template, request
from database import carregar_vagas_db
from database import carregar_vaga_db

app = Flask(__name__)



@app.route("/")
def home():
    vagas = carregar_vagas_db()
    return  render_template('home.html', vagas=vagas)

@app.route("/vagas")
def lista_vagas():
    vagas = carregar_vagas_db()
    return jsonify(vagas)

@app.route("/vaga/<id>")
def mostra_vaga(id):
    vaga = carregar_vaga_db(id)
    return render_template('detalhevaga.html', vaga=vaga)

@app.route("/vaga/<id>/formulario", methods=['GET','POST'])
def formulario_vaga(id):
    data = request.form
    return jsonify(data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

