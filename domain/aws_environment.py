class AwsEnvironment:
    def __init__(self, db_database='', db_host='', db_port='', db_user_id='', db_user_pass='', available_years=[],
                 question_difficulties={}, bncc_sas_host='', difficulties_parameters=[]):
        self.db_database = db_database
        self.db_host = db_host
        self.db_port = db_port
        self.db_user_id = db_user_id
        self.db_user_pass = db_user_pass
        self.available_years = available_years
        self.question_difficulties = question_difficulties
        self.bncc_sas_host = bncc_sas_host
        self.difficulties_parameters = difficulties_parameters
