from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators	import DataRequired

class PostForm(FlaskForm):
	blog_entry = StringField('Write Your Entry', validators=[DataRequired()])
	submit = SubmitField('Post Blog')
