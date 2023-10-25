# Importando bibliotecas necessárias
import timeit
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Inicializando a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

# Declarando uma classe de modelo para o banco de dados usando SQLAlchemy
Base = declarative_base()


class Cadastro(Base):
    __tablename__ = "cadastros"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(255))
    telefone = Column(Integer)
    observacao = Column(Text)

    def __repr__(self):
        return f"<Cadastro(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone}, observacao={self.observacao})>"


# Criando o mecanismo de banco de dados e tabelas
engine = create_engine("sqlite:///cadastros.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# Função para inserir dados no banco de dados
def insert_data():
    session = Session()
    for i in range(10000):
        cadastro = Cadastro(
            nome=f"Nome {i}",
            email=f"email{i}@example.com",
            telefone=123456789,
            observacao=f"Observacao {i}",
        )
        session.add(cadastro)
    session.commit()
    session.close()


# Função principal para inserir dados e consultar registros
def main():
    # Medindo o tempo de inserção dos dados no banco de dados
    start_time = timeit.default_timer()
    insert_data()
    end_time = timeit.default_timer()
    print(f"tempo_de_insercao: {1000 * (end_time - start_time)} ms")

    # Medindo o tempo de consulta dos registros do banco de dados
    start_time = timeit.default_timer()
    consultar_cadastros()
    end_time = timeit.default_timer()
    print(f"tempo_de_consulta: {1000 * (end_time - start_time)} ms")


# Função para consultar os registros do banco de dados
def consultar_cadastros():
    start_time = timeit.default_timer()
    session = Session()
    registros = session.query(Cadastro).all()
    session.close()
    end_time = timeit.default_timer()
    tempo_execucao = 1000 * (end_time - start_time)  # Convertendo para milissegundos
    return registros, tempo_execucao


# Rota principal da aplicação
@app.route('/')
def index():
    # Consulta os registros do banco de dados
    cadastros, tempo_execucao = consultar_cadastros()

    # Converte os registros para o formato JSON
    cadastros_json = [
        {
            'id': cadastro.id,
            'nome': cadastro.nome,
            'email': cadastro.email,
            'telefone': cadastro.telefone,
            'observacao': cadastro.observacao
        }
        for cadastro in cadastros
    ]

    # Cria uma resposta JSON com os registros e o tempo de execução
    response = {
        'cadastros': cadastros_json,
        'tempo_execucao': tempo_execucao
    }

    # Retorna a resposta JSON
    return jsonify(response)


# Inicializa a aplicação Flask e executa a função main()
if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    main()
    app.run()
