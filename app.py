from flask import Flask, render_template

app = Flask(__name__)

app.config(
    SECRET_KEY = "j234jkl23j"
)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')