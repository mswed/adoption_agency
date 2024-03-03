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

    @app.route('/add')
    def add_pet():
        form = PetForm()
        return render_template('new_pet.html', form=form)

    return app


flask_app = create_app()
