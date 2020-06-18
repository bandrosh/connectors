from domain import DbConnector
from db_connectors import MsSqlConnector


def main():
    db_connector = DbConnector()

    mssql_connector = MsSqlConnector(db_connector)

    # Example
    # questions_enem = mssql_connector.get_data_query('SELECT * FROM BancoDeQuestoes_BNCC.dbo.VestibularesQuestoes')

if __name__ == "__main__":
    main()
