from app.models import User
from app.db import Session, Base, engine 

# This is where the db variables that you created earlier come into play. 
# The code uses the Base class together with the engine connection variable to do two things. 
#   First, it drops all the existing tables. 
#   Second, it creates any tables that Base mapped, in a class that inherits Base (like User).


# drop and rebuild tables 
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# run: python seeds.py

# Anytime we want to perform a CRUD operation using SQLAlchemy, we need to establish a temporary session connection with the Session class. 
db = Session()
 
# insert users
#  within this db session object, we use the add_all() method and the User model to create several new users.
#  Note: db.add_all() alone doesn't change the database. In fact, it only preps the SQL queries.
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])
# To run the INSERT statements, you need to call db.commit()
db.commit()

# If you don't need to make any other database transactions at this time, you can close the session connection by calling db.close().
db.close()