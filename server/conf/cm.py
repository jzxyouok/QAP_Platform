# coding: utf8


class ConfigManager:
    def __init__(self):
        # self.env = "production"
        self.env = "development"
        self.config = {
            "development": {
                "mysql": {
                    "host": "localhost",
                    "user": "root",
                    "passwd": "flyfishdb",
                    "db": "Question_Answer_Platform",
                    "charset": "utf8"
                },
                "redis": {
                    "host": "localhost",
                    "port": 6379
                }
            }
        }

    def get_dbconfig(self):
        db_config = self.config[self.env]["mysql"]
        return db_config

    def get_config(self, name):
        config = self.config[self.env][name]
        return config
