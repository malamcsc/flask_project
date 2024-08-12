import os

# Values to be used during development. Here you might specify the URI of a database sitting on localhost.

# Statement for enabling the development environment
#test change

DB_USER = os.environ.get("DB_USER","postgres")
DB_PASS = os.environ.get("DB_PASS","root@123")
#POSTGRES_URL = os.environ.get("POSTGRES_URL","localhost:5433")
INSTANCE_HOST = os.environ.get("INSTANCE_HOST","localhost")
DB_NAME = os.environ.get("DB_NAME","flaskdb")
DB_PORT = os.environ.get("DB_PORT","5433")

DB_URL = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(user=DB_USER,pw=DB_PASS,host=INSTANCE_HOST,port =DB_PORT, db=DB_NAME)
print(DB_URL)

SQLALCHEMY_DATABASE_URI = DB_URL





