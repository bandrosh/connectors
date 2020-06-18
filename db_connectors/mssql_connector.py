import pandas as pd
import pymssql


class MsSqlConnector:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def get_data_query(self, query):

        connection_string = pymssql.connect(server=self.db_connector.host, port=self.db_connector.port,
                                            user=self.db_connector.user_id, password=self.db_connector.user_pass,
                                            database=self.db_connector.database)
        return pd.read_sql_query(query, connection_string)
