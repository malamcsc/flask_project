import os

# Values to be used during development. Here you might specify the URI of a database sitting on localhost.

# Statement for enabling the development environment

POSTGRES_USER = os.environ.get("POSTGRES_USER","flask_user")
POSTGRES_PW = os.environ.get("POSTGRES_PW","flask")
POSTGRES_URL = os.environ.get("POSTGRES_URL","localhost:5433")
#POSTGRES_URL = os.environ.get("POSTGRES_URL","172.30.144.1:5433")
POSTGRES_DB = os.environ.get("POSTGRES_DB","flaskdb")

DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

SQLALCHEMY_DATABASE_URI = DB_URL





