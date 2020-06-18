class DbConnector:
    def __init__(self, database, host, port, user_id, user_pass):
        self.database = database
        self.host = host
        self.port = port
        self.user_id = user_id
        self.user_pass = user_pass
