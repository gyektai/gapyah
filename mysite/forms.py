from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators	import DataRequired, Length

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	blog_writer = StringField('Write Your Entry', validators=[DataRequired()])
	submit = SubmitField('Post Blog')

class GuestForm(FlaskForm):
	guest = StringField('Sign Your Name', validators=[DataRequired(), Length(min=1, max=30)])
	message = StringField('Leave a Message')
	submit = SubmitField('Sign!')
