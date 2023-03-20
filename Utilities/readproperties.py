import configparser

config = configparser.RawConfigParser()
config.read(".\\Configs\\config.ini")

class readconfig():
    @staticmethod
    def getbaseurl():
        url = config.get('Common data','baseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get('Common data','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Common data','password')
        return password