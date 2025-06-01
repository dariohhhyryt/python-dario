from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# String de conexão com host e porta corretos
string_conexao = (
    "mysql+pymysql://root:FuHzSLdgzwYChUrMXPwRresbyNUBLsqE@mainline.proxy.rlwy.net:46396/railway?charset=utf8mb4"
)
engine = create_engine(string_conexao)


def carregar_vagas_db():
    with engine.connect() as connection:
        resultado = connection.execute(text("SELECT * FROM vagas"))
        vagas = []
        for row in resultado.mappings(): 
            vagas.append(dict(row))
    return vagas

   

