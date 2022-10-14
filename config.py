# The class is created for the configurations
class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = 'architecture-project.mysql.database.azure.com'
    MYSQL_USER = 'admi@architecture-project'
    MYSQL_PASSWORD = 'Eman_2021'
    MYSQL_DB = 'proyect'


# The configurations are exported as a dictionary
config = {
    'development': DevelopmentConfig
}