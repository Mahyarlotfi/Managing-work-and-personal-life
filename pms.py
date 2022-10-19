from unicodedata import name
from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)