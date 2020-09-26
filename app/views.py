from flask import render_template,request,redirect,url_for,abort
from app import app
from .models import Pitch, User
from .forms import UpdateProfile
from flask_login import login_required
from . import db, photos

Pitch = Pitch



@app.route('/', methods = ['GET','POST'])
def index():
    pitches = Pitch.query.all()
    return render_template('index.html', pitches=pitches)




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

@app.route('/category/<category>',methods= ['GET', 'Post'])
def pitches_by_category(category):
    category_pitches = Pitch.query.filter_by(category=category)

    return render_template('category.html', pitches=category_pitches)