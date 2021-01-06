from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "hard to guess string"

##
## Forms
##
class EnterYourInfos(FlaskForm):
    name = StringField("Enter your name :", validators= [DataRequired()])
    age = IntegerField("Enter your age :", validators= [DataRequired(), NumberRange(min=10, max=100)])
    sex = SelectField("Sex", choices= [('0', 'Homme'), ('1', 'Femme')], validators= [InputRequired([('0', 'Homme'), ('1', 'Femme')])], coerce= int)
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<name>')
def welcome_name(name):
    return render_template('custom_hello.html', name= name)

@app.route('/<int:age>')
def welcome_age(age):
    return "<h1>Hello {}</h1>".format(age)

@app.route('/prediction', methods= ["GET", "POST"])
def prediction_form():
    form = EnterYourInfos()
    if request.method == "POST" and form.validate_on_submit(): # request is available only within a decorated func
        # import joblib
        # model = joblib.load('models/nomModel')
        # session['results'] = model.predict([.....])
        return redirect("/results")
    return render_template('prediction_form.html', form= form)
    
@app.route("/results")
def results():
    return render_template('results.html', results= session['results'])

if __name__ == "__main__":
    # run server
    print(app.url_map)
    app.run(host= "0.0.0.0", port= 5000, debug= True)