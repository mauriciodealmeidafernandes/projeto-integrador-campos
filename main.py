from flask import Flask, jsonify, make_response, request
# Importa o banco de dados
from bd import Campos

# Instanciar o modulo Flask na nossa variavel app
app = Flask("campos")

# PRIMEIRO METODO - VISUALIZAR OS DADOS (GET)
# app.route -> definir que essa funcao e uma rota para que o flask entenda queilo precisa ser executado.
@app.route("/campos", methods=["GET"])
def get_campos():
    return Campos 

# PRIMEIRO METODO PARTE 2 - VISUALIZAR DADOS POR ID (GET/ID)
@app.route("/campos/<int:id>",methods=["GET"])
def get_campos_id(id):
    for campos in Campos:
        if campos.get("id") == id:
            return jsonify(campos)
# SEGUNDO METODO - CRIR NOVOS DADOS (POST)
@app.route("/campos", methods=["POST"])
def criar_campos():  
    objetoRecebido = request.json
    Campos.append(objetoRecebido)
    return make_response(jsonify(mensagem="Campos cadastrado com sucesso", campos=objetoRecebido))  
            

# TERCEIRO METODO - EDITAR DADOS (PUT)
@app.route("/campos/<int:id>",methods = ["PUT"])
def editar_campos_id(id):
    campos_alterado = request.get_json()
    for indice, campos in enumerate(Campos):      
        if campos.get("id") == id:
            Campos[indice].update(campos_alterado)
            return jsonify(Campos[indice])
#QUARTO METODO - DELETAR DADOS (DELETE)
@app.route("/campos/<int:id>", methods=["DELETE"])
def excluir_campos(id):
    for indice, campos in enumerate(Campos):
        if campos.get("id") == id:
            del Campos[indice]
            return jsonify({"mensagem:": "Campos excluido com sucesso"})

app.run(port=5000, host="localhost")