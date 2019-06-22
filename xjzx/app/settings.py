
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask0'

def make_database_url(fun):
    dialect = fun.get('dialect') or 'mysql'
    driver = fun.get('driver') or 'pymysql'
    username = fun.get('username') or 'root'
    password = fun.get('password') or 'root'
    host = fun.get('host') or 'localhost'
    port =  fun.get('port') or '3306'
    database =  fun.get('database') or 'flask0'

    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,username,password,host,port,database)




class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = '120'
    SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopMent(Config):
    DEBUG = True

    database = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'root',
        'host':'localhost',
        'port':'3306',
        'database':'flask0',
    }

    SQLALCHEMY_DATABASE_URI = make_database_url(database)


class TESTing(Config):
    TESTing = True

    database = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'database': 'flask0',
    }

    SQLALCHEMY_DATABASE_URI = make_database_url(database)


class Show(Config):

    database = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'database': 'flask0',
    }

    SQLALCHEMY_DATABASE_URI = make_database_url(database)


class Product(Config):

    database = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'database': 'flask0',
    }

    SQLALCHEMY_DATABASE_URI = make_database_url(database)


config_env={
    'development':DevelopMent,
    'testing':TESTing,
    'show':Show,
    'product':Product
}