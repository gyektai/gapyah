from flask import render_template, url_for, redirect
from mysite import app
from mysite.forms import PostForm
from mysite.models import Post


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