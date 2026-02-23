from flask import Blueprint, render_template, session
from app.models import User, Cart, Code,Chat, Product

main = Blueprint("main", __name__)

@main.route("/")
def home():
    if not session.get("id"):
        return render_template("home.html", logged_in=False)
    id=session.get("id")
    user=User.query.filter_by(id=id).first()
    cartCount=Chat.query.filter_by(sender_id=id).count()
    notCount=Product.query.filter_by(id=id).count()
    notfications = Product.query.all()
    fullname=user.name
    splitName=fullname.split()
    fname=splitName[0]
    
    return render_template("home.html", logged_in=True, fname=fname,cartCount=cartCount,notCount=notCount, notfications=notfications)
    
    