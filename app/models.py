from app.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ ="users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.Boolean, nullable=False, default=False)
    profile_pic = db.Column(db.String(100), nullable=True, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)


class Chat(db.Model):
    __tablename__="chats"
    id = db.Column(db.Integer(), primary_key=True)
    sender_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(), nullable=False)
    file = db.Column(db.String(), nullable=True)
    sent_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    sender = db.relationship("User", foreign_keys=[sender_id], backref=db.backref("sent_chats", lazy=True))
    receiver = db.relationship("User", foreign_keys=[receiver_id], backref=db.backref("received_chats", lazy=True))

class Code(db.Model):
    __tablename__ ="codes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    is_used = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)

class Category(db.Model):
    __tablename__="categories"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Integer, nullable=False, unique=True)

class Product(db.Model):
    __tablename__="products"
    id=db.Column(db.Integer, primary_key=True)
    category_id=db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    price=db.Column(db.Float, nullable=False)
    stock=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String,nullable=False, unique=True)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Cart(db.Model):
    __tablename__="carts"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id=db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity=db.Column(db.Integer, nullable=False, default=0)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    
    



