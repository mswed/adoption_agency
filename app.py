from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import PetForm


def create_app(database='adopt', echo=True, csrf=True):
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
        form = PetForm()
        if form.validate_on_submit():
            new_pet = Pet(name=form.name.data,
                          species=form.species.data,
                          photo_url=form.photo_url.data,
                          age=form.age.data,
                          notes=form.notes.data)
            db.session.add(new_pet)
            db.session.commit()
            return redirect('/')
        else:
            return render_template('new_pet.html', form=form)

    @app.route('/<int:pet_id>', methods=['GET', 'POST'])
    def show_pet(pet_id):
        pet = Pet.query.get(pet_id)
        form = PetForm(obj=pet)
        if form.validate_on_submit():
            pet = Pet.query.get(pet_id)
            pet.photo_url = form.photo_url.data
            pet.notes = form.notes.data
            pet.available = form.available.data
            db.session.add(pet)
            db.session.commit()

            return redirect('/')
        else:
            return render_template('show_pet.html', form=form, pet=pet)
    return app


flask_app = create_app()
