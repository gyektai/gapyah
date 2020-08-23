from datetime import datetime
from mysite import db

class Post(db.Model):
	title = db.Column(db.String, nullable=False, primary_key=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"