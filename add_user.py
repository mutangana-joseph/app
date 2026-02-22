from app.extensions import db
from app.models import User
from app import create_app
app = create_app()

with app.app_context():
    new_user = User.query.all()
    for user in new_user:
        print(user.name, user.email)


    