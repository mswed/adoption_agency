from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import PetForm


def create_app(database='adopt', echo=True, csrf=True):
    """
    Create a flask app
    :param database: str, name of database
    :param echo: bool, should sql statements be printed?
    :param csrf: bool, should wtform csrf run?
    :return: Instance(Flask), a flask app
    """
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{database}'
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SECRET_KEY'] = 'something_safe_for_sure'
    app.config['WTF_CSRF_ENABLED'] = csrf

    connect_db(app)

    @app.route('/')
    def home_page():
        """
        Show a list of all pets
        :return: render_template, list of pets
        """
        pets = Pet.query.all()
        return render_template('home.html', pets=pets)

    @app.route('/add', methods=['GET', 'POST'])
    def add_pet():
        """
        Create a new pet
        """
        form = PetForm()
        # Validate the form (also check if this is a post request)
        if form.validate_on_submit():
            # Post request, create a new pet and redirect to root
            form_data = form.data
            form_data.pop('csrf_token', None)
            new_pet = Pet(**form_data)
            db.session.add(new_pet)
            db.session.commit()

            return redirect('/')
        else:
            # Get request, return the same page
            return render_template('new_pet.html', form=form)

    @app.route('/<int:pet_id>', methods=['GET', 'POST'])
    def show_pet(pet_id):
        """
        Display / edit pet info
        :param pet_id: int, id of the pet in the database
        """
        # Get a pet and a form
        pet = Pet.query.get(pet_id)
        form = PetForm(obj=pet)

        # Validate the fields
        if form.validate_on_submit():
            # This is a post request, grab the pet info and update its fields
            pet.photo_url = form.photo_url.data
            pet.notes = form.notes.data
            pet.available = form.available.data
            db.session.add(pet)
            db.session.commit()

            return redirect('/')
        else:
            # This is a get request show the pet info
            return render_template('show_pet.html', form=form, pet=pet)
    return app


flask_app = create_app()
