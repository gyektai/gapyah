from flask import Flask, render_template
from forms import PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c702f92f9d7843302720201f994eb10'

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='GY for Gap Year')

@app.route('/makepost')
def makepost():
	form = PostForm()
	return render_template('write.html', title='Make Post', form=form)


if __name__ == '__main__':
	app.run(debug=True)

