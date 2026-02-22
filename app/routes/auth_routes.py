from flask import Blueprint, render_template, request,  redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from app.models import User, Code
from flask_mail import Message
from app.config import Config
from app.extensions import db
from app import mail
import random





auth = Blueprint("auth", __name__)




@auth.route("/sign/in", methods=["GET", "POST"])
def signIn():

    if request.method=="POST":
        emailInput=request.form["emailInput"]
        passwordInput=request.form["passwordInput"]

        our_user=User.query.filter_by(email=emailInput).first()

        if our_user and check_password_hash(our_user.password, passwordInput):
            session["user_id"] = our_user.password
            return redirect(url_for("main.home"))
        flash("Invalid credentials.", "error")
        return redirect(url_for("auth.signIn"))

        flash("User doesn't exist", "error")
        return redirect(url_for("auth.signIn"))

    return render_template("auth.html", signIn=True)




@auth.route("/sign/up", methods=["GET", "POST"])
def signUp():

    if request.method =="POST":

        nameInput=request.form['nameInput']
        emailInput=request.form["emailInput"]
        passwordInput=request.form["passwordInput"]
        hashedPassword=generate_password_hash(passwordInput)
        exist_email=User.query.filter_by(email=emailInput).first()

        if exist_email:
            flash("Email already exist", "error")
            return redirect(url_for("auth.signUp"))

        if nameInput.casefold() in passwordInput.casefold() or emailInput.casefold() in passwordInput.casefold():
            flash("Password should not be similar to your name or email", "error")
            return redirect(url_for("auth.signUp"))

        if len(passwordInput) < 6:
            flash("Your password should be at least 6 charcters", "error")
            return redirect(url_for("auth.signUp"))

        if not any(char.isdigit() for char in passwordInput):
            flash("You password is missing a digit", "error")
            return redirect(url_for("auth.signUp"))
        

        new_user=User(name=nameInput, email=emailInput, password=hashedPassword)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.signIn"))


    return render_template("auth.html", signUp=True)




@auth.route("/reset/password", methods=["GET", "POST"])
def resetPassword():
    if request.method == "POST":

        emailInput=request.form["emailInput"]
        user=User.query.filter_by(email=emailInput).first()

        if user:

            userId = user.id
            name=user.name
            recipientEmail=user.email
            new_code = random.randint(100000, 999999)
            expires_date = datetime.utcnow() + timedelta(minutes=10)

            new_row=Code(user_id=userId, code=new_code, expires_at=expires_date)
            session["user_reset_id"] = user.id
            db.session.add(new_row)
            db.session.commit()

            msg = Message(
                "Shoppingapp Password Reset",
                recipients=[recipientEmail]
            ) 
            
            msg.body = f"your one time code is: {new_code}"  
            msg.html = f"""
            <span><h1 style="font-size:small;">Hello, {name}</h1> </span>
            <p>Your one time code is: <strong>{new_code}</strong></p>
            <br>This code will expire in 10 minutes.</br>
            """
            mail.send(msg)

            return render_template("auth.html", resetCode=True)
        flash("Something went wrong. Try again.", "error")
        return redirect(url_for("auth.resetPassword"))
    return render_template("auth.html", resetPassword=True)





@auth.route("/reset/code", methods=["GET", "POST"])
def resetCode():

    session_id = session.get("user_reset_id")

    if not session_id:
        return render_template("404.html")

    if request.method == "POST":  
        code = request.form["code"]
        current_time = datetime.utcnow()
        valid_code = Code.query.filter(Code.expires_at > current_time, Code.user_id==session_id, Code.code==code).first()
        
        if valid_code:
            valid_code.is_used=True
            Code.query.filter_by(user_id=session_id).delete()
            db.session.commit()
            return render_template("auth.html", newPassword=True)

        flash("No data found. Request new code", "error")
        return redirect(url_for("auth.resetPassword"))
    return render_template("auth.html", resetCode=True)


@auth.route("/new/password" , methods=["GET", "POST"])
def newPassword():

    
    session_id = session.get("user_reset_id")

    if not session_id:
        return render_template("404.html")
    if request.method=="POST":

        passwordInput=request.form["passwordInput"]
        confirmPass=request.form["confirmPass"]
        user=User.query.filter_by(id=session_id).first()

        if user.name.casefold() in passwordInput.casefold() or user.email.casefold() in passwordInput.casefold():
            flash("Password should not be similar to your name or email", "error")
            return redirect(url_for("auth.newPassword"))

        if len(confirmPass) < 6:
            flash("Your password should be at least 6 charcters", "error")
            return redirect(url_for("auth.newPassword"))

        if not any(char.isdigit() for char in passwordInput):
            flash("You password is missing a digit","error")
            return redirect(url_for("auth.newPassword"))

        if passwordInput == confirmPass and user:
            new_hash=generate_password_hash(confirmPass)

            user.password=new_hash
            db.session.commit()
            session.clear()
            flash("Your new password is successfully created", "success")
            return redirect(url_for("auth.signIn")) 
            
        flash("Please enter same password value in fields", "error")
        return redirect(url_for("auth.newPassword"))
    return render_template("auth.html", newPassword=True)