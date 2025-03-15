
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
dados_dic={}
CORS(app)


def carregar_pizzas(url_path):
    with open(url_path,  "r") as arq:
        return json.load(arq)

_pizzas=carregar_pizzas("pizzas.json")


@app.route("/", methods=["GET", "PUT"])
def get_dados():
    if request.method=="PUT":
        date=request.get_json()

        for key, value in date.items():
            dados_dic[key]=value
    return dados_dic

@app.route("/pizzas", methods=["GET", "PUT"])
def get_pizzas():
    if request.method=="PUT":
        date=request.get_json()

        for key, value in date.items():
            _pizzas[key]=value
    return _pizzas

@app.route("/receber", methods=["POST"])
def response_front():
    response_date=request.json
    print(response_date)

    msgObj={"Sucesso": "Update realizado com sucesso"}
    return jsonify(msgObj), 200

if __name__=="__main__":
    app.run()