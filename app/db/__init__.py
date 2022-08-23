from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# because we used a .env file to fake the environment variable, we need to first call load_dotenv() from the python-dotenv module. 
# In production, DB_URL will be a proper environment variable.
load_dotenv()

# connect to database using env variable

# The engine variable manages the overall connection to the database.
    # Note: the getenv() function is part of Python's built-in os module.
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# The Session variable generates temporary connections for performing create, read, update, and delete (CRUD) operations
Session = sessionmaker(bind=engine)
# The Base class variable helps us map the models to real MySQL tables.
Base = declarative_base()

def init_db(app):
    # using 'Base' methods from seeds.py, but call it after init_db(), to call when the flask app is ready.
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)


# whenever this function is called, it returns a new session-connection object. Other modules in the app can import Session directly from the db package, 
# but using a function means that we can perform additional logic before creating the database connection.
def get_db():
    if 'db' not in g:
        # store db connection in app context; The get_db() function now saves the current connection on the g object, if it's not already there.
        g.db = Session()

    return g.db

# leverage flask context to close the db connection
def close_db(e=None):
    # The pop() method attempts to find and remove db from the g object. 
    db  = g.pop('db', None)
    # If db exists (that is, db doesn't equal None), then db.close() will end the connection.
    if db is not None: 
        db.close()
        # The close_db() function won't run automatically, though. We need to tell Flask to run it whenever a context is destroyed.