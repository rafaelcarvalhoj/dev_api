from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


tarefas = [
    {
        'id': '0',
        'status': 'nao concluida',
        'tarefa': 'limpar o banheiro'
    }
]


@app.route('/', methods=['GET', 'PUT'])
def tarefa():
    if request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas.append(dados)
        return jsonify({'status': 'adicionada com sucesso'})


@app.route('/<int:id>', methods=['GET', 'PUT'])
def listar_tarefa(id):
    if request.method == 'GET':
        try:
            return jsonify(json.loads(tarefas[id]))
        except IndexError:
            return jsonify({'status':'erro', 'mensagem': f'tarefa id={id} nao existe'})
    elif request.method == 'PUT':
        try:
            if tarefas[id]['status'] == 'nao concluida':
                tarefas[id]['status'] = 'concluida'
            else:
                tarefas[id]['status'] = 'nao concluida'
            return jsonify({'status': 'sucesso', 'mesagem': 'status da tarefa mudado com sucesso'})
        except IndexError:
            return jsonify({'status': 'erro', 'mensagem': f'tarefa id={id} nao existe'})


if __name__ == '__main__':
    app.run()
