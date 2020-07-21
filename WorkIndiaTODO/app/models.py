from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from datetime import datetime

@login.user_loader
def load_user(id):
    return user.query.get(int(id))

class user(UserMixin,db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<user {}>'.format(self.id)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class todo(db.Model):
    title = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(140))
    category = db.Column(db.String(140))
    due_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title) 