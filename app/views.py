from flask import render_template,request,redirect,url_for,abort
from app import app
from .models import Pitch, User
from .forms import PitchForm, UpdateProfile
from flask_login import login_required
from . import db,photos

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

@app.route('/user/<uname>', methods = ['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

    return render_template("profile/profile.html", user = user, form=form)

@app.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@app.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('profile',uname=uname))