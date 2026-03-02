from flask import Blueprint, render_template, session, request
from app.models import User, Product, Category
from app.extensions import db
from app.config import Config
from werkzeug.exceptions import RequestEntityTooLarge
from flask import Blueprint, render_template, session, redirect, url_for, g
from app.models import User, Product, Category, Chat
import uuid, os
from werkzeug.utils import secure_filename


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

@admin.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(error):
    flash("File too large! Max size is 16 MB.")
    return  redirect(url_for("admin.add_product"))


@admin.route("/")
def admin_home():
    return render_template("admin.html", name=g.name)

   
@admin.route("/sign/out")
def signOut():
    session.clear()
    return redirect(url_for("main.home"))

@admin.route("/add-product", methods=["POST", "GET"])
def add_product():

    if request.method=="POST":

        category=request.form["category"]
        name=request.form["name"]
        price=request.form["price"]
        stock=request.form["stock"]
        desc=request.form["desc"]
        file=request.files["file"]

        
        if file:

            if secure_filename(file.filename) == '':
                return "No file selected"
                
            ext=os.path.splitext(secure_filename(file.filename))[1]


            if ext not in [".png", ".jpg", ".jpeg"]:
                return "File not supported. Supported file's extensions are ['.jpg', '.png', 'jpeg']"
            unique_name=f"{uuid.uuid4().hex[:16]}{ext}"
            upload_path=os.path.join(Config.PRODUCT_PIC_FOLDER, unique_name)
            file.save(upload_path)
            newProduct=Product(name=name, category_id=category, description=desc, price=price, stock=stock, image=unique_name)
            db.session.add(newProduct)
            db.session.commit()
            return "Product Added"

        return "No file selected"


    return render_template("add-product.html", name=g.name)

@admin.route("/add-category", methods=["POST", "GET"])
def add_category():
    if request.method == "POST":

        name=request.form["name"]
        newCategory = Category(name=name)
        db.session.add(newCategory)
        db.session.commit()
        return redirect(url_for('admin.add_category'))
    return render_template("add_category.html", name=g.name)

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
    return render_template("display-product.html", name=g.name, products=products)


@admin.route("/display/category")
def display_category():
    categories=Category.query.all()
    return render_template("display_category.html", categories=categories, name=g.name)