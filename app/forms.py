from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required, DataRequired

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[DataRequired()])
    pitch = TextAreaField('Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')