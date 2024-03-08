from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from App.database import db

class User(db.Model):
    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True)
    #need a usertype

    #user details
    username =  db.Column(db.String, nullable=False, unique=True) #using this as staff/student ID
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(120), nullable=False)
        
    #faculty/dept info
    #faculty
    #department
    #campus

    #house
    
    
    
    

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class UserType(db.Model):
    pass