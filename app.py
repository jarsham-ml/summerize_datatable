from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms import FileField, SubmitField

app = Flask(__name__)

app.config(
    SECRET_KEY = "j234jkl23j"
)

class fileForm(FlaskForm):
    xlsxfile = ileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')