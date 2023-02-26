from flask_restful import Resource
from flask import request
import json


lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']


# Listar e remover habilidades
class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    mensagem_erro = {'status': 'erro', 'mensagem': 'erro ao adicionar/mudar habilidade, procure um administrador da api'}
    def post(self):
        try:
            dados = json.loads(request.data)
            lista_habilidades.append(dados['habilidade'])
            return {'status': 'sucesso', 'mensagem': 'habilidade adicionada com sucesso'}
        except Exception:
            return self.mensagem_erro


    def put(self):
        try:
            dados = json.loads(request.data)
            lista_habilidades[dados['id']] = dados['habilidade']
            return {'status': 'sucesso', 'mensagem': 'habilidade mudada'}
        except IndexError:
            dados = json.loads(request.data)
            return {'status': 'erro', 'mensagem': f'habilidade nao encontrada no id{dados["id"]}'}
        except Exception:
            return self.mensagem_erro


class DeletarHabilidade(Resource):
    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            return {'status': 'sucesso', 'mensagem': 'Registro excluido'}
        except IndexError:
            return {'status': 'erro', 'mensagem': f'habilidade nao encontrada no index{id}'}