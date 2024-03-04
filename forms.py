from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField, BooleanField
from wtforms.validators import Optional, NumberRange, URL


class PetForm(FlaskForm):
    """
    Create a pet form
    """
    name = StringField("Pet's name")
    species = SelectField('Species', choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = URLField('Photo URL', validators=[URL(message='This is not a valid URL!'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = StringField('Notes')
    available = BooleanField('Available?')
