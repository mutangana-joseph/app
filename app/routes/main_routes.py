from flask import Blueprint, render_template, session, jsonify
from app.models import User, Cart, Code,Chat, Product
import time

main = Blueprint("main", __name__)

@main.route("/")
def home():
    products=Product.query.order_by(Product.created_at.desc()).all()

    if not session.get("id"):
        return render_template("home.html", logged_in=False, products=products)
    id=session.get("id")
    user=User.query.filter_by(id=id).first()
    cartCount=Chat.query.filter_by(sender_id=id).count()
    notfications = Product.query.all()
    notCount=len(notfications)
    fullname=user.name
    splitName=fullname.split()
    fname=splitName[0]
    
    return render_template("home.html", logged_in=True, fname=fname,cartCount=cartCount,notCount=notCount, notfications=notfications, products=products)
    

@main.route("/products")
def get_products():

    time.sleep(1)
    products = Product.query.order_by(Product.created_at.desc()).all()
    return jsonify([p.dict() for p in products])

@main.route("/search")
def search():
    time.sleep(3)
    user=User.query(id=1).first()
    return jsonify([p.dict() for p in user])