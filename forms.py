from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField
from wtforms.validators import Optional, NumberRange, URL


class PetForm(FlaskForm):
    name = StringField("Pet's name")
    species = SelectField('Species', choices=['cat', 'dog', 'porcupine'])
    photo_url = URLField('Photo URL', validators=[URL(message='This is not a valid URL!'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = StringField('Notes')
