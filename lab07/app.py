import os
from flask import Flask, render_template, request
import segno

app = Flask(__name__)

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code_path = None
    user_input = None

    if request.method == "POST":
        user_input = request.form.get("data")
        if user_input:
            qr_code_path = os.path.join(STATIC_FOLDER, "qr_code.png")
            qr = segno.make(user_input)
            qr.save(qr_code_path, scale=8)
            qr_code_path = "qr_code.png"

    return render_template("index.html", qr_code=qr_code_path, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)

    app.run(debug=True)
