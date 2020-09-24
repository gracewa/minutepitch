from flask import render_template, request, url_for, redirect
from app import app
from .models import Pitch
from .forms import PitchForm
from flask_login import login_required

Pitch = Pitch



@app.route('/', methods = ['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')

    elif request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')



@app.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()

    if form.validate_on_submit():
            title = form.title.data
            pitch = form.pitch.data
            pitch = Pitch(id,title,pitch)
            pitch.save_pitch()
            return redirect(url_for('pitch',id = pitch.id ))

    return render_template('pitch.html', pitch_form=form)
