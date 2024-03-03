from app import create_app
from models import db, Pet

create_app()

flask_app = create_app()

with flask_app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Pet(name='Mango',
             species='cat',
             photo_url='https://en.wikipedia.org/wiki/File:Cat_November_2010-1a.jpg',
             age=3,
             notes='He is a cat!')

    db.session.add(p1)
    db.session.commit()
