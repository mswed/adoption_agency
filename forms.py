from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField


class PetForm(FlaskForm):
    name = StringField("Pet's name")
    species = StringField('Species')
    photo_url = URLField('Photo URL')
    age = IntegerField('Age')
    notes = StringField('Notes')