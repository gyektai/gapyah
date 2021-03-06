from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators	import DataRequired, Length

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	blog_writer = TextAreaField('Write Your Entry', validators=[DataRequired()])
	submit = SubmitField('Post Blog')

class GuestForm(FlaskForm):
	guest = StringField('Sign Your Name', validators=[DataRequired(), Length(min=1, max=30)])
	message = TextAreaField('Leave a Message', validators=[Length(max=120)])
	submit = SubmitField('Sign')
