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
        'NAME' : 'controlcuentas_database',
        'USER' : 'root1',
        'PASSWORD' : 'root1',
        'HOST' : 'localhost',
        
    }
}
MYSQL3 = {
    'default':{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'cont',
        'USER' : 'root1',
        'PASSWORD' : 'root1',
        'HOST' : 'localhost',
        
    }
}