from flask import Flask, render_template
from utils import generate_message

app = Flask(__name__)

@app.route("/")
def index():
    message = generate_message()
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run()
