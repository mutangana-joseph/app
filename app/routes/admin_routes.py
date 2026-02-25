from flask import Blueprint, render_template, session
from app.models import User
admin = Blueprint("admin", __name__, url_prefix='/admin')

from flask import Blueprint, render_template, session, redirect, url_for, g
from app.models import User, Product, Category, Chat

admin = Blueprint("admin", __name__, url_prefix='/admin')


@admin.before_request
def check_admin():
    if not session.get("id"):
        return render_template("404.html")

    user = User.query.get(session.get("id"))
    if not user or not user.role :
        return render_template("404.html")
  
    g.user = user
    g.name = user.name.split()[0]


@admin.route("/")
def admin_home():
   
    return render_template("admin.html",name=g.name)
   
@admin.route("/sign/out")
def signOut():
    session.clear()
    return redirect(url_for("main.home"))

@admin.route("/add-product")
def add_product():
    if not session.get("id"):
        return render_template("404.html")
    return render_template("add-product.html",)

@admin.route("/dashboard")
def dashboard():
    userCount=User.query.count()
    pCount=Product.query.count()
    catCount=Category.query.count()
    msgCount=Chat.query.filter_by(receiver_id=session.get("id"), is_read=False).count()
    return render_template("dashboard.html", name=g.name, userCount=userCount, pCount=pCount, catCount=catCount, msgCount=msgCount)


@admin.route("/display/product")
def displayProduct():
    
    products=Product.query.all()

    return render_template("display-product.html", name=g.name)