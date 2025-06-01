from sqlalchemy import create_engine, text
from sqlalchemy.engine import connection_memoize
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

def carregar_vaga_db(id):
 with engine.connect() as connection:
    resultado = connection.execute(text(f"SELECT * FROM vagas WHERE id = :val"),                                  {"val": id})
    registro = resultado.mappings().all()
    if len(registro) == 0:
      return None
    else:
      return dict(registro[0])

