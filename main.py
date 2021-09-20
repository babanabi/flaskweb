##############  Libraries ##############
from flask import Flask, render_template, redirect ,request, flash, url_for
from flask_wtf import FlaskForm
from wtforms.validators import Length, Email, DataRequired
from wtforms import StringField, SubmitField , TextAreaField
from flask_sqlalchemy import SQLAlchemy
import os


#############   Configurations   ##############
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = '0x229fc71d6'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'databs.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)




#############   Flaskform   ##############
class ContactForm(FlaskForm):

    fullname = StringField(label='fullname', validators=[DataRequired()])
    email = StringField(label='email', validators=[DataRequired(), Email()])
    source = StringField(label='source')
    budget = StringField(label='budget')
    text = TextAreaField(label='text',validators=[DataRequired(),Length(min=2,max=500)])
    submit = SubmitField(label='Send')



######   Database class   ###########################
class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    source = db.Column(db.String())
    budget = db.Column(db.Integer())
    text = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"User: {self.fullname}, Contact: {self.email}, Source: {self.source}, Budget: {self.budget}, Content: {self.text} "



##############  Routes  #################

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/video")
def video_page():
    return render_template("video.html")

@app.route("/graphic_design")
def graphic_page():
    return render_template("graphic.html")

@app.route("/contact", methods=['GET','POST'])
def contact_page():
    form = ContactForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            mes = User(fullname = form.fullname.data,
                            email = form.email.data,
                            source = form.source.data,
                            budget = form.budget.data,
                            text = form.text.data)
            if form.fullname.data == "baba":
                db.create_all()
            
            db.session.add(mes)
            db.session.commit()

            message = "Your message was successfully sent. We well back you soon"
            flash(message, category='success')
            return redirect(url_for('home_page'))  
    
 

    return render_template('contact.html', form=form, )


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route("/gallery")
def gallery_page():
    return render_template("gallery.html")

##############  Album routes ##############
@app.route("/album1")
def album1_page():
    return render_template("album1.html")

@app.route("/album2")
def album2_page():
    return render_template('album2.html')

@app.route("/album3")
def album3_page():
    return render_template('album3.html')

@app.route("/album4")
def album4_page():
    return render_template('album4.html')

@app.route("/album5")
def album5_page():
    return render_template('album5.html')    

@app.route("/album6")
def album6_page():
    return render_template('album6.html')   

@app.route("/album7")
def album7_page():
    return render_template('album7.html')   

@app.route("/album8")
def album8_page():
    return render_template('album8.html') 


    

##############   Error Handler #################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



##############  RUNNING #################
if __name__ == "__main__":
    app.run( port=8000, host="0.0.0.0")