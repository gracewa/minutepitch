from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitch', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):

    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch = db.Column(db.String)
    category = db.Column(db.String)
    posted = db.Column(db.Time,default=datetime.now())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_pitches(cls,id):

        pitches = Pitch.query.filter_by(id=id).all()
        return pitches