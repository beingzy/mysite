#class Config(object):
#	DEBUG = False
#	TESTING = False
#	SECRET_KEY = '1234883'
#	USERNAME = 'admin'
#	PASSWORD = 'default'
    #MONGO_DB = 'beingzy_site'
#    MONGO_HOST = '0.0.0.0'
#    MONGO_PORT = 27017


# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'
# 
# class DevelopmentConfig(Config):
#     DEBUG = True
#     MONGO_HOST = '54.88.134.182'

# class TestingConfig(Config):
#     TESTING = True
#     MONGO_HOST = '54.88.134.182'

class Config(object):
    DEBUG   = False
    TESTING = False
    HOST    = '0.0.0.0'
    PORT    = 8000
    MONGODB_SETTINGS = {
    'DB': "beingzy_site", 
    'HOST': '0.0.0.0',
    'PORT': 27017
    }

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True
	MONGODB_SETTINGS = {
    'DB': "beingzy_site", 
    'HOST': '54.88.134.182',
    'PORT': 27017
    }

class TestConfig(Config):
	TESTING = True
	MONGODB_SETTINGS = {
    'DB': "beingzy_site", 
    'HOST': '54.88.134.182',
    'PORT': 27017
    }
