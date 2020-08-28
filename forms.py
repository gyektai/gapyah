from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators	import DataRequired

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	blog_writer = StringField('Write Your Entry', validators=[DataRequired()])
	submit = SubmitField('Post Blog')
