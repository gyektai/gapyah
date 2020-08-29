from datetime import datetime
from mysite import db

class Post(db.Model):
	title = db.Column(db.String, nullable=False, primary_key=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

class Guest(db.Model):
	name = db.Column(db.String, nullable=False, primary_key=True)
	message = db.Column(db.Text, nullable=True)
	date_signed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Post('{self.name}', '{self.date_signed}')"