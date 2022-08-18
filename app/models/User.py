from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt 

salt = bcrypt.gensalt()


# create the User model that inherits the Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates('email') #decorator
    def validate_email(self, key, email): 
        # make sure email address contains @ character 
        #   the assert keyword to check if an email address contains an at-sign character (@). 
        #   The assert keyword automatically throws an error if the condition is false, thus preventing the return statement from happening.
        assert '@' in email 

        return email
    
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4

        # encrypt password
        return bcrypt.hashpw(password.encode('UTF-8'), salt)