from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

def conectarDB():
    return mysql.connector.connect(
        host='turntable.proxy.rlwy.net',
        port='49484',
        user='root',
        password='enPMNsBoFjfqnBMyXIgdDHAVNorOSQUF',
        database='funilaria_bdd'
    )

def formatarData(data):
    partes = data.split('/')
    dataFormatada =  f"{partes[2]}-{partes[1]}-{partes[0]}"
    return dataFormatada




# ------------------------------| CLIENTES |------------------------------ #


@app.route('/clientes', methods=['POST'])
def criarClientes():
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        item = request.json
    
        sql =   f"INSERT INTO clientes VALUES "\
                f"(null, "\
                f"'{item['nome']}', "\
                f"'{formatarData(item['datanasc'])}', "\
                f"'{item['rg']}', "\
                f"'{item['cpf']}', "\
                f"'{item['telefone']}', "\
                f"'{item['sexo']}') "

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/clientes/<int:id>', methods=['PUT'])
def editarClientes(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        item = request.json

        sql =   f"UPDATE clientes SET "\
                f"nome='{item['nome']}', "\
                f"datanasc='{formatarData(item['datanasc'])}', "\
                f"rg='{item['rg']}', "\
                f"cpf='{item['cpf']}', "\
                f"telefone='{item['telefone']}', "\
                f"sexo='{item['sexo']}' "\
                f"WHERE id_cliente={id} "

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluirClientes(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
    
        sql = f"DELETE FROM clientes WHERE id_cliente={id}"

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/clientes', methods=['GET'])
def listarClientes():
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql = f"SELECT *, DATE_FORMAT(datanasc, '%d/%m/%Y') FROM clientes"

        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = list()
        for i in resultado:
            item.append(
                {
                    'id_cliente': i[0],  
                    'nome': i[1],  
                    'datanasc': i[7],
                    'rg': i[3],
                    'cpf': i[4],
                    'telefone': i[5],
                    'sexo': i[6]
                }
            )
        return jsonify(item)
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/clientes/<int:id>', methods=['GET'])
def listarClientesID(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        
        sql = f"SELECT *, DATE_FORMAT(datanasc, '%d/%m/%Y') FROM clientes WHERE id_cliente={id}"

        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = list()
        for i in resultado:
            item.append(
                {
                    'id_cliente': i[0],    
                    'nome': i[1],
                    'datanasc': i[7],
                    'rg': i[3],
                    'cpf': i[4],
                    'telefone': i[5],
                    'sexo': i[6]
                }
            )
        return jsonify(item)
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()




# ------------------------------| VEICULOS |------------------------------ #


@app.route('/veiculos', methods=['POST'])
def criarVeiculos():
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        item = request.json

        sql =   f"INSERT INTO veiculos VALUES "\
                f"(null, "\
                f"'{item['fabricante']}', "\
                f"'{item['modelo']}', "\
                f"'{item['ano']}', "\
                f"'{item['placa']}', "\
                f"'{item['cliente']}')"

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/veiculos/<int:id>', methods=['PUT'])
def editarVeiculos(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        item = request.json

        sql =   f"UPDATE veiculos SET "\
                f"fabricante='{item['fabricante']}', "\
                f"modelo='{item['modelo']}', "\
                f"ano='{item['ano']}', "\
                f"placa='{item['placa']}' "\
                f"WHERE id_veiculo={id} "

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/veiculos/<int:id>', methods=['DELETE'])
def excluirVeiculos(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql = f"DELETE FROM veiculos WHERE id_veiculo={id}"

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/veiculos', methods=['GET'])
def listarVeiculos():
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql = f"SELECT * FROM veiculos"

        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = list()
        for i in resultado:
            item.append(
                {
                    'id_veiculo': i[0],  
                    'fabricante': i[1],
                    'modelo': i[2],
                    'ano': i[3],
                    'placa': i[4],
                    'cliente': i[5]
                }
            )
        return jsonify(item)
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/veiculos/<int:id>', methods=['GET'])
def listarVeiculosID(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql = f"SELECT * FROM veiculos WHERE id_veiculo={id}"

        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = list()
        for i in resultado:
            item.append(
                {
                    'id_veiculo': i[0],           
                    'fabricante': i[1],
                    'modelo': i[2],
                    'ano': i[3],
                    'placa': i[4],
                    'cliente': i[5]
                }
            )
        return jsonify(item)
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()




# ------------------------------| SERVICOS |------------------------------ #


@app.route('/ordemservico', methods=['POST'])
def criarServicos():
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        item = request.json

        sql =   f"INSERT INTO ordemServico VALUES "\
                f"(null, "\
                f"'{item['tiposerv']}', "\
                f"'{item['valorserv']}', "\
                f"'{formatarData(item['dataini'])}', "\
                f"'{formatarData(item['datafim'])}', "\
                f"'{item['cliente']}', "\
                f"'{item['veiculo']}')"

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/ordemservico/<int:id>', methods=['PUT'])
def editarServicos(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()
        item = request.json

        sql =   f"UPDATE ordemServico SET "\
                f"tiposerv='{item['tiposerv']}', "\
                f"valorserv='{item['valorserv']}', "\
                f"dataini='{formatarData(item['dataini'])}', "\
                f"datafim='{formatarData(item['datafim'])}' "\
                f"WHERE id_ordemServico={id} "

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/ordemservico/<int:id>', methods=['DELETE'])
def excluirServicos(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql = f"DELETE FROM ordemServico WHERE id_ordemServico={id}"

        cursor.execute(sql)
        conexao.commit()
        return {'Mensagem': "OPERAÇÃO REALIZADA COM SUCESSO"}
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/ordemservico', methods=['GET'])
def listarServicos():
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql =   f"SELECT *, DATE_FORMAT(os.dataini, '%d/%m/%Y'), DATE_FORMAT(os.datafim, '%d/%m/%Y'), DATE_FORMAT(c.datanasc, '%d/%m/%Y') FROM ordemServico AS os "\
                f"INNER JOIN clientes AS c ON os.cliente = c.id_cliente "\
                f"INNER JOIN veiculos AS v ON os.veiculo = v.id_veiculo "
        
        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = list()
        for i in resultado:
            item.append(
                {
                    'id_ordemServico': i[0],
                    'tiposerv': i[1],
                    'valorserv': i[2],
                    'dataini': i[20],
                    'datafim': i[21],

                    'id_cliente': i[7],
                    'nome': i[8],
                    'datanasc': i[22],
                    'rg': i[10],
                    'cpf': i[11],
                    'telefone': i[12],
                    'sexo': i[13],

                    'id_veiculo': i[14],
                    'fabricante': i[15],
                    'modelo': i[16],
                    'ano': i[17],
                    'placa': i[18]
                }
            )
        return jsonify(item)
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()


@app.route('/ordemservico/<int:id>', methods=['GET'])
def listarServicosID(id):
    try:
        conexao = conectarDB()
        cursor = conexao.cursor()

        sql =   f"SELECT *, DATE_FORMAT(os.dataini, '%d/%m/%Y'), DATE_FORMAT(os.datafim, '%d/%m/%Y'), DATE_FORMAT(c.datanasc, '%d/%m/%Y') FROM ordemServico AS os "\
                f"INNER JOIN clientes AS c ON os.cliente = c.id_cliente "\
                f"INNER JOIN veiculos AS v ON os.veiculo = v.id_veiculo "\
                f"WHERE os.id_ordemServico={id} "
        
        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = list()
        for i in resultado:
            item.append(
                {
                    'id_ordemServico': i[0],
                    'tiposerv': i[1],
                    'valorserv': i[2],
                    'dataini': i[20],
                    'datafim': i[21],

                    'id_cliente': i[7],
                    'nome': i[8],
                    'datanasc': i[22],
                    'rg': i[10],
                    'cpf': i[11],
                    'telefone': i[12],
                    'sexo': i[13],

                    'id_veiculo': i[14],
                    'fabricante': i[15],
                    'modelo': i[16],
                    'ano': i[17],
                    'placa': i[18]
                }
            )
        return jsonify(item)
    except:
        return {'Erro': "NAO FOI POSSIVEL REALIZAR ESSA OPERACAO"}
    finally:
        cursor.close()
        conexao.close()





# --------| MAIN |-------- #
if __name__ == '__main__':
    app.run(debug=True)