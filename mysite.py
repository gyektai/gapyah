from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c702f92f9d7843302720201f994eb10'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Post(db.Model):
	title = db.Column(db.String, nullable=False, primary_key=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"


@app.route('/home')
@app.route('/')
def home():
	posts = Post.query.all()
	return render_template('home.html', title='GY for Gap Year', posts=posts)

@app.route('/makepost', methods=['GET', 'POST'])
def makepost():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.blog_writer.data)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('write.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)

