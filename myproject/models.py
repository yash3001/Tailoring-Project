from myproject import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    ph_number = db.Column(db.Text)
    length_shirt = db.Column(db.Text)
    chest_shirt = db.Column(db.Text)
    waist_shirt = db.Column(db.Text)
    shoulder_shirt = db.Column(db.Text)
    hips_shirt = db.Column(db.Text)
    neck_shirt = db.Column(db.Text)
    sleeves_shirt = db.Column(db.Text)
    flair_shirt = db.Column(db.Text)
    slit_shirt = db.Column(db.Text)
    armhole_shirt = db.Column(db.Text)
    biceps_shirt = db.Column(db.Text)
    front_shirt = db.Column(db.Text)
    back_shirt = db.Column(db.Text)
    length_trouser = db.Column(db.Text)
    poncha_trouser = db.Column(db.Text)
    length_blouse = db.Column(db.Text)
    chest_blouse = db.Column(db.Text)
    shoulder_blouse = db.Column(db.Text)
    neck_blouse = db.Column(db.Text)
    sleeves_blouse = db.Column(db.Text)
    armhole_blouse = db.Column(db.Text)
    biceps_blouse = db.Column(db.Text)
    plate_blouse = db.Column(db.Text)
    extra_1 = db.Column(db.Text)
    extra_2 = db.Column(db.Text)
    extra_3 = db.Column(db.Text)
    extra_4 = db.Column(db.Text)

    def __init__(self, name, address, ph_number, length_shirt,
                 chest_shirt, waist_shirt, shoulder_shirt, hips_shirt, neck_shirt,
                 sleeves_shirt, flair_shirt, slit_shirt, armhole_shirt, biceps_shirt,
                 front_shirt, back_shirt, length_trouser, poncha_trouser, length_blouse,
                 chest_blouse, shoulder_blouse, neck_blouse, sleeves_blouse, armhole_blouse,
                  biceps_blouse, plate_blouse, extra_1, extra_2, extra_3, extra_4):

        self.name  = name
        self.address = address
        self.ph_number = ph_number
        self.length_shirt = length_shirt
        self.chest_shirt = chest_shirt
        self.waist_shirt = waist_shirt
        self.shoulder_shirt = shoulder_blouse
        self.hips_shirt = hips_shirt
        self.neck_shirt = neck_shirt
        self.sleeves_shirt = sleeves_shirt
        self.flair_shirt = flair_shirt
        self.slit_shirt = slit_shirt
        self.armhole_shirt = armhole_shirt
        self.biceps_shirt = biceps_shirt
        self.front_shirt = front_shirt
        self.back_shirt = back_shirt
        self.length_trouser = length_trouser
        self.poncha_trouser = poncha_trouser
        self.length_blouse = length_blouse
        self.chest_blouse  = chest_blouse
        self.shoulder_blouse = shoulder_blouse
        self.neck_blouse = neck_blouse
        self.sleeves_blouse = sleeves_blouse
        self.armhole_blouse = armhole_blouse
        self.biceps_blouse = biceps_blouse
        self.plate_blouse = plate_blouse
        self.extra_1 = extra_1
        self.extra_2 = extra_2
        self.extra_3 = extra_3
        self.extra_4 = extra_4
