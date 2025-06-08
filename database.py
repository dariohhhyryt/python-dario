from sqlalchemy import create_engine, text, values
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
        

def formulario_vaga(id_vaga, dado):
    with engine.connect() as connection: 
        
        query = text(f"INSERT INTO formulario_vaga (id_vaga, nome, email, linkedin, experiencia) VALUES (:id_vaga, :nome, :email, :linkedin, :experiencia)")

        connection.execute(

            query, {
                "vaga_id": id_vaga,
                "nome": dados["nome"],
                "email": dados["email"],
                "linkedin": dados["linkedin"],
                "experiencia": dados["experiencia"]
            } )

        connection.commit()  # Garante que a alteração seja persistida










