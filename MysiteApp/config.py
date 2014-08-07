class Config(object):
    DEBUG   = False
    TESTING = False
    HOST    = '0.0.0.0'
    PORT    = 80
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
