from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI
import mysql.connector
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*']
)

sql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='funilaria_bdd'
)

conexao = sql
cursor = conexao.cursor()





# ------------------------------| CLIENTES |------------------------------ #

class Cliente (BaseModel):
    nome: str
    datanasc: str
    rg: str
    cpf: str
    telefone: str
    sexo: str


@app.post("/clientes")
async def criarClientes(item: Cliente):
    cursor.execute(f"INSERT INTO clientes (nome, datanasc, rg, cpf, telefone, sexo) VALUES ('{item.nome}', '{item.datanasc}', '{item.rg}', '{item.cpf}', '{item.telefone}', '{item.sexo}')")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.put("/clientes/{id}")
async def editarClientes(item: Cliente, id: int):
    cursor.execute(f"UPDATE clientes SET nome='{item.nome}', datanasc='{item.datanasc}', rg='{item.rg}', cpf='{item.cpf}', telefone='{item.telefone}', sexo='{item.sexo}' WHERE id={id}")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.delete("/clientes/{id}")
async def excluirClientes(id: int):
    cursor.execute(f"DELETE FROM clientes WHERE id={id}")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.get("/clientes")
async def listarClientes():
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

    return JSONResponse(content=jsonable_encoder(item))


@app.get("/clientes/{id}")
async def listarClientesID(id: int):
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

    return JSONResponse(content=jsonable_encoder(item))





# ------------------------------| VEICULOS |------------------------------ #

class Veiculo (BaseModel):
    fabricante: str
    modelo: str
    ano: str
    placa: str


@app.post("/veiculos")
async def criarVeiculos(item: Veiculo):
    cursor.execute(f"INSERT INTO veiculos (fabricante, modelo, ano, placa) VALUES ('{item.fabricante}', '{item.modelo}', '{item.ano}', '{item.placa}')")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.put("/veiculos/{id}")
async def editarVeiculos(item: Veiculo, id: int):
    cursor.execute(f"UPDATE veiculos SET fabricante='{item.fabricante}', modelo='{item.modelo}', ano='{item.ano}', placa='{item.placa}' WHERE id={id}")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.delete("/veiculos/{id}")
async def excluirVeiculos(id: int):
    cursor.execute(f"DELETE FROM veiculos WHERE id={id}")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.get("/veiculos")
async def listarVeiculos():
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

    return JSONResponse(content=jsonable_encoder(item))


@app.get("/veiculos/{id}")
async def listarVeiculosID(id: int):
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

    return JSONResponse(content=jsonable_encoder(item))





# ------------------------------| SERVICOS |------------------------------ #

class Servico (BaseModel):
    tiposerv: str
    valorserv: str
    dataini: str
    datafim: str


@app.post("/servicos")
async def criarServicos(item: Servico):
    cursor.execute(f"INSERT INTO servicos (tiposerv, valorserv, dataini, datafim) VALUES ('{item.tiposerv}', '{item.valorserv}', '{item.dataini}', '{item.datafim}')")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.put("/servicos/{id}")
async def editarServicos(item: Servico, id: int):
    cursor.execute(f"UPDATE servicos SET tiposerv='{item.tiposerv}', valorserv='{item.valorserv}', dataini='{item.dataini}', datafim='{item.datafim}' WHERE id={id}")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.delete("/servicos/{id}")
async def excluirServicos(id: int):
    cursor.execute(f"DELETE FROM servicos WHERE id={id}")
    conexao.commit()
    return {"mensagem": "OPERAÇÃO REALIZADA COM SUCESSO"}


@app.get("/servicos")
async def listarServicos():
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

    return JSONResponse(content=jsonable_encoder(item))


@app.get("/servicos/{id}")
async def listarServicosID(id: int):
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

    return JSONResponse(content=jsonable_encoder(item))






if __name__ == "__main__":
    uvicorn.run(app, port=8080)

cursor.close()
conexao.close()