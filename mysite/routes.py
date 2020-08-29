from flask import render_template, url_for, redirect
from mysite import app, db
from mysite.forms import PostForm, GuestForm
from mysite.models import Post, Guest


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title='GY for Gap Year')

@app.route('/makepost', methods=['GET', 'POST'])
def makepost():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.blog_writer.data)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('write.html', form=form)

@app.route('/layout')
def layout():
	return render_template('layout.html', title='GY Gap Year')

@app.route('/blog')
def blog():
	posts = Post.query.all()
	return render_template('blog.html', title='GY Blog', posts=posts)

@app.route('/projects')
def projects():
	return render_template('projects.html', title='GY Projects')

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
	form = GuestForm()
	if form.validate_on_submit():
		guest = Guest(name=form.guest.data, message=form.message.data)
		db.session.add(guest)
		db.session.commit()
		return redirect(url_for('guestbook'))
	guests = Guest.query.all()
	return render_template('guestbook.html', title='GY Guest Book', guests=guests, form=form)