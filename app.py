from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


desenvolvedores = [
    {'id': '0',
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']},
    {'id': '1',
     'nome': 'Carvalho',
     'habilidades': ['Python', 'Django']}
]


# devolve um desenvolvedor pelo ID e tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'desenvolvedor de ID {id} nao existe'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'erro desconhecido, procure um administrador da API'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})


# lista todos os desenvolvedores e permite o registro de um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run()