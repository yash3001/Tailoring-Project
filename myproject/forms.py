from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):

    name = StringField('Name:', validators=[DataRequired()])
    address = StringField('Address:', validators = [DataRequired()])
    ph_number = IntegerField('Phone Number:', validators = [DataRequired()])
    length_shirt = StringField('Length:')
    chest_shirt = StringField('Chest:')
    waist_shirt = StringField('Waist')
    shoulder_shirt = StringField('Shoulder:')
    hips_shirt = StringField('Hips:')
    neck_shirt = StringField('Neck:')
    sleeves_shirt = StringField('Sleeves:')
    flair_shirt = StringField('Flair:')
    slit_shirt = StringField('Slit:')
    armhole_shirt = StringField('Armhole:')
    biceps_shirt = StringField('Biceps:')
    front_shirt = StringField('Front:')
    back_shirt = StringField('Back:')
    length_trouser = StringField('Length:')
    poncha_trouser = StringField('Poncha:')
    length_blouse = StringField('Length:')
    chest_blouse  = StringField('Chest:')
    shoulder_blouse = StringField('Shoulder:')
    neck_blouse = StringField('Neck:')
    sleeves_blouse = StringField('Sleeves:')
    armhole_blouse = StringField('Armhole:')
    biceps_blouse = StringField('Biceps:')
    plate_blouse = StringField('Plate:')
    extra_1 = StringField('Extra 1:')
    extra_2 = StringField('Extra 2:')
    extra_3 = StringField('Extra 3:')
    extra_4 = StringField('Extra 4', validators = [DataRequired()])
    submit = SubmitField('Submit')

class SearchId(FlaskForm):
    id = IntegerField('Enter the id of the customer: ', validators = [DataRequired()])
    submit = SubmitField('Search')

class SearchName(FlaskForm):
    name = StringField('Enter the name of the customer:', validators = [DataRequired()])
    submit = SubmitField('Search')

class SearhPhNumber(FlaskForm):
    ph_number = IntegerField('Enter the phone number of the cutomer:',validators = [DataRequired()])
    submit = SubmitField('Search')

class DeleteCustomer(FlaskForm):
    id = IntegerField('Enter the id of the customer:', validators = [DataRequired()])
    submit = SubmitField('Delete')

class ModifyCustomer(FlaskForm):
    id = IntegerField('Enter the Id of the customer to be modified:', validators = [DataRequired()])
    name = StringField('Name:', validators=[DataRequired()])
    address = StringField('Address:')
    ph_number = IntegerField('Phone Number:')
    length_shirt = StringField('Length:')
    chest_shirt = StringField('Chest:')
    waist_shirt = StringField('Waist')
    shoulder_shirt = StringField('Shoulder:')
    hips_shirt = StringField('Hips:')
    neck_shirt = StringField('Neck:')
    sleeves_shirt = StringField('Sleeves:')
    flair_shirt = StringField('Flair:')
    slit_shirt = StringField('Slit:')
    armhole_shirt = StringField('Armhole:')
    biceps_shirt = StringField('Biceps:')
    front_shirt = StringField('Front:')
    back_shirt = StringField('Back:')
    length_trouser = StringField('Length:')
    poncha_trouser = StringField('Poncha:')
    length_blouse = StringField('Length:')
    chest_blouse  = StringField('Chest:')
    shoulder_blouse = StringField('Shoulder:')
    neck_blouse = StringField('Neck:')
    sleeves_blouse = StringField('Sleeves:')
    armhole_blouse = StringField('Armhole:')
    biceps_blouse = StringField('Biceps:')
    plate_blouse = StringField('Plate:')
    extra_1 = StringField('Extra 1:')
    extra_2 = StringField('Extra 2:')
    extra_3 = StringField('Extra 3:')
    extra_4 = StringField('Extra 4', validators = [DataRequired()])
    submit = SubmitField('Update')

class LoginForm(FlaskForm):
    username = StringField('Username:')
    password = PasswordField('Password')
    submit = SubmitField('Login')
