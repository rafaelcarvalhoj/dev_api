from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, DeletarHabilidade
import json

app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {'id': '0',
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']},
    {'id': '1',
     'nome': 'Carvalho',
     'habilidades': ['Python', 'Django']}
]


# devolve um desenvolvedor pelo ID e tambem altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'desenvolvedor de ID {id} nao existe'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'erro desconhecido, procure um administrador da API'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


# lista todos os desenvolvedores e permite o registro de um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'mensagem': 'registro inserido'}

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(DeletarHabilidade, '/habilidades/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
