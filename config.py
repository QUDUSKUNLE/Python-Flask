# config.py

class config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class developmentConfig(config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class productionConfig(config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {'development': developmentConfig, 'production': productionConfig}
