from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

railway = mysql.connector.connect(
    host='turntable.proxy.rlwy.net',
    user='root',
    password='enPMNsBoFjfqnBMyXIgdDHAVNorOSQUF',
    database='funilaria_bdd'
)

conexao = railway
cursor = conexao.cursor()





# ------------------------------| CLIENTES |------------------------------ #


@app.route('/clientes', methods=['POST'])
def criarClientes():
    item = request.json
    cursor.execute(f"INSERT INTO clientes (nome, datanasc, rg, cpf, telefone, sexo) VALUES ('{item['nome']}', '{item['datanasc']}', '{item['rg']}', '{item['cpf']}', '{item['telefone']}', '{item['sexo']}')")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/clientes/<int:id>', methods=['PUT'])
def editarClientes(id):
    item = request.json
    cursor.execute(f"UPDATE clientes SET nome='{item['nome']}', datanasc='{item['datanasc']}', rg='{item['rg']}', cpf='{item['cpf']}', telefone='{item['telefone']}', sexo='{item['sexo']}' WHERE id={id}")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluirClientes(id):
    cursor.execute(f"DELETE FROM clientes WHERE id={id}")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/clientes', methods=['GET'])
def listarClientes():
    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()

    item = list()
    for i in resultado:
        item.append(
            {
                'id': i[0],  
                'nome': i[1],  
                'datanasc': i[2],
                'rg': i[3],
                'cpf': i[4],
                'telefone': i[5],
                'sexo': i[6]
            }
        )
    return jsonify(item)


@app.route('/clientes/<int:id>', methods=['GET'])
def listarClientesID(id):
    cursor.execute(f"SELECT * FROM clientes WHERE id={id}")
    resultado = cursor.fetchall()

    item = list()
    for i in resultado:
        item.append(
            {
                'id': i[0],    
                'nome': i[1],
                'datanasc': i[2],
                'rg': i[3],
                'cpf': i[4],
                'telefone': i[5],
                'sexo': i[6]
            }
        )
    return jsonify(item)





# ------------------------------| VEICULOS |------------------------------ #


@app.route('/veiculos', methods=['POST'])
def criarVeiculos():
    item = request.json
    cursor.execute(f"INSERT INTO veiculos (fabricante, modelo, ano, placa) VALUES ('{item['fabricante']}', '{item['modelo']}', '{item['ano']}', '{item['placa']}')")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/veiculos/<int:id>', methods=['PUT'])
def editarVeiculos(id):
    item = request.json
    cursor.execute(f"UPDATE veiculos SET fabricante='{item['fabricante']}', modelo='{item['modelo']}', ano='{item['ano']}', placa='{item['placa']}' WHERE id={id}")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/veiculos/<int:id>', methods=['DELETE'])
def excluirVeiculos(id):
    cursor.execute(f"DELETE FROM veiculos WHERE id={id}")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/veiculos', methods=['GET'])
def listarVeiculos():
    cursor.execute("SELECT * FROM veiculos")
    resultado = cursor.fetchall()

    item = list()
    for i in resultado:
        item.append(
            {
                'id': i[0],  
                'fabricante': i[1],
                'modelo': i[2],
                'ano': i[3],
                'placa': i[4]
            }
        )
    return jsonify(item)


@app.route('/veiculos/<int:id>', methods=['GET'])
def listarVeiculosID(id):
    cursor.execute(f"SELECT * FROM veiculos WHERE id={id}")
    resultado = cursor.fetchall()

    item = list()
    for i in resultado:
        item.append(
            {
                'id': i[0],           
                'fabricante': i[1],
                'modelo': i[2],
                'ano': i[3],
                'placa': i[4]
            }
        )
    return jsonify(item)





# ------------------------------| SERVICOS |------------------------------ #

@app.route('/servicos', methods=['POST'])
def criarServicos():
    item = request.json
    cursor.execute(f"INSERT INTO servicos (tiposerv, valorserv, dataini, datafim) VALUES ('{item['tiposerv']}', '{item['valorserv']}', '{item['dataini']}', '{item['datafim']}')")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/servicos/<int:id>', methods=['PUT'])
def editarServicos(id):
    item = request.json
    cursor.execute(f"UPDATE servicos SET tiposerv='{item['tiposerv']}', valorserv='{item['valorserv']}', dataini='{item['dataini']}', datafim='{item['datafim']}' WHERE id={id}")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/servicos/<int:id>', methods=['DELETE'])
def excluirServicos(id):
    cursor.execute(f"DELETE FROM servicos WHERE id={id}")
    conexao.commit()
    return {'mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.route('/servicos', methods=['GET'])
def listarServicos():
    cursor.execute("SELECT * FROM servicos")
    resultado = cursor.fetchall()

    item = list()
    for i in resultado:
        item.append(
            {
                'id': i[0],
                'tiposerv': i[1],
                'valorserv': i[2],
                'dataini': i[3],
                'datafim': i[4]
            }
        )
    return jsonify(item)


@app.route('/servicos/<int:id>', methods=['GET'])
def listarServicosID(id):
    cursor.execute(f"SELECT * FROM servicos WHERE id={id}")
    resultado = cursor.fetchall()

    item = list()
    for i in resultado:
        item.append(
            {
                'id': i[0],
                'tiposerv': i[1],
                'valorserv': i[2],
                'dataini': i[3],
                'datafim': i[4]
            }
        )
    return jsonify(item)





if __name__ == '__main__':
    app.run(port=49484, debug=True)

cursor.close()
conexao.close()