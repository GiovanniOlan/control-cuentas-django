import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


MYSQL = {
    'default':{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'controlcuentas_database',
        'USER' : 'root',
        'PASSWORD' : '753963',
        'HOST' : 'localhost',
        
    }
}
MYSQL2 = {
    'default':{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'concuee',
        'USER' : 'root',
        'PASSWORD' : '753963',
        'HOST' : 'localhost',
        
    }
}