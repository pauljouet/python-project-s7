from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange
import numpy as np

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "hard to guess string"

features = np.genfromtxt('python-project-s7/data/X_test.csv',delimiter=',')
##
## Forms
##
class EnterYourInfos(FlaskForm):
    name = StringField("Enter your name :", validators= [DataRequired()])
    age = IntegerField("Enter your age :", validators= [DataRequired(), NumberRange(min=10, max=100)])
    sex = SelectField("Sex", choices= [('0', 'Homme'), ('1', 'Femme')], validators= [InputRequired([('0', 'Homme'), ('1', 'Femme')])], coerce= int)
    submit = SubmitField("Submit")

class ChooseSong(FlaskForm):
    song = SelectField("Song", choices= [('0', 'Song 1'),('1', 'Song 2'),('2', 'Song 3'),('3', 'Song 4'),('4', 'Song 5'),('5', 'Song 6')], 
    validators=[InputRequired([('0', 'Song 1'), ('1', 'Song 2'),('2', 'Song 3'),('3', 'Song 4'),('4', 'Song 5'),('5', 'Song 6')])], coerce= int)
    model= SelectField("Model", choices= [('python-project-s7/models/model1_sgd_epochs100', 'SGD model'), ('python-project-s7/models/model2_adam_tuned_epochs30', 'Adam model')],
    validators=[InputRequired([('python-project-s7/models/model1_sgd_epochs100', 'SGD model'), ('python-project-s7/models/model2_adam_tuned_epochs30', 'Adam model')])], coerce=str)
    submit= SubmitField('Confirm')

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/prediction', methods= ["GET", "POST"])
def prediction_form():
    form = EnterYourInfos()
    if request.method == "POST" and form.validate_on_submit(): # request is available only within a decorated func
        
        session['username'] = form.name.data
        session['age'] = form.age.data
        session['sex'] = form.sex.data
        return redirect("/choose_song")
    return render_template('prediction_form.html', form= form)

@app.route('/choose_song', methods= ["GET", "POST"])
def choose_song():
    form = ChooseSong()
    if request.method == "POST" and form.validate_on_submit():
        
        chosen_song = features[form.song.data]
        from keras.models import load_model
        chosen_model = load_model(form.model.data)
        session['results'] = int((chosen_model.predict(chosen_song[np.newaxis,:]) * 89) + 1922)
        return redirect("/results")
    return render_template('choose_song.html', form=form)
    
@app.route("/results")
def results():
    return render_template('results.html', results= session['results'], age = session['age'], name= session['username'], sex=session['sex'])

if __name__ == "__main__":
    # run server
    print(app.url_map)
    app.run(host= "0.0.0.0", port= 5000, debug= True)