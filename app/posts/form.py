from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class PostForm(FlaskForm):
    title = TextAreaField('', validators=[DataRequired()], render_kw={
        "placeholder": "Post#"}, widget=TextArea())
    content = StringField('', validators=[DataRequired()], render_kw={
        "placeholder": "Content#"}, widget=TextArea())
    submit = SubmitField("Submit")
