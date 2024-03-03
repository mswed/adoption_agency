from app import create_app
from models import db, Pet

create_app()

flask_app = create_app()

with flask_app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Pet(name='Mango',
             species='cat',
             photo_url='https://th-thumbnailer.cdn-si-edu.com/bgmkh2ypz03IkiRR50I-UMaqUQc=/1000x750/filters:no_upscale():focal(1061x707:1062x708)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/55/95/55958815-3a8a-4032-ac7a-ff8c8ec8898a/gettyimages-1067956982.jpg',
             age=3,
             notes='He is a cat!')

    p2 = Pet(name='Kitten',
             species='cat',
             photo_url='https://wallup.net/wp-content/uploads/2018/10/06/708149-kittens-kitten-cat-cats-baby-cute-s.jpg',
             age=1,
             notes='So small!')

    db.session.add_all([p1, p2])
    db.session.commit()
