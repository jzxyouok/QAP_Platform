# coding: utf8


class ConfigManager:
    def __init__(self):
        # self.env = "development"
        self.env = "production"
        self.config = {
            "development": {
                "mysql": {
                    "host": "192.168.1.106",
                    "user": "root",
                    "passwd": "asd123",
                    "db": "Question_Answer_Platform",
                    "charset": "utf8"
                },
                "redis": {
                    "host": "192.168.1.106",
                    "port": 6379
                },
                "upload": {
                    "save": {
                        "pic": "/data/upload/pic/",
                        "avatar": "/data/upload/avatar/",
                        "sound": "/data/upload/sound/"
                    },
                    "visit": {
                        "pic": "/qap_server/uploads/question/pic/",
                        "avatar": "/qap_server/uploads/user/avatar/",
                        "sound": "/qap_server/uploads/question/sound/"
                    }
                }
            },
            "production": {
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
                },
                "upload": {
                    "save": {
                        "pic": "/data/upload/pic/",
                        "avatar": "/data/upload/avatar/",
                        "sound": "/data/upload/sound/"
                    },
                    "visit": {
                        "pic": "/qap_server/uploads/question/pic/",
                        "avatar": "/qap_server/uploads/user/avatar/",
                        "sound": "/qap_server/uploads/question/sound/"
                    }
                }
            }
        }

    def get_dbconfig(self):
        db_config = self.config[self.env]["mysql"]
        return db_config

    def get_config(self, name):
        config = self.config[self.env][name]
        return config
