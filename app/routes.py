from flask import render_template ,url_for ,flash ,redirect ,request
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)