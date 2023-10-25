from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Cadastro  # Importe sua classe Cadastro do módulo correto

engine = create_engine("sqlite:///cadastros.db")
Session = sessionmaker(bind=engine)


def delete_data():
    session = Session()

    # Use uma consulta para selecionar registros com ID maior que 10000
    registros_para_deletar = session.query(Cadastro).filter(Cadastro.id > -1)

    # Exclua os registros selecionados
    registros_para_deletar.delete(synchronize_session=False)

    # Comite/aplique as alterações
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_data()
