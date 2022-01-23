import os

#Variables for getting constanbt values from os
db_host=os.environ.get('DB_HOST', default='10.0.1.210') #Database private IP
db_name=os.environ.get('DB_NAME', default='dashboard')
db_password=os.environ.get('DB_PASSWORD', default='secure_password')
db_port=os.environ.get('DB_PORT', default='5432')
db_user=os.environ.get('DB_USER', default='dashboard')

SQLALCHEMY_DATABASE_URI= f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"