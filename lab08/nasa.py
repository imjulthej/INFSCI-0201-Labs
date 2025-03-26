from flask import Flask, render_template, request
from apod_api import get_apod
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    apod_data = get_apod()
    return render_template("index.html", apod=apod_data)

@app.route("/history", methods=["GET", "POST"])
def history():
    apod_data = None
    error_message = None

    if request.method == "POST":
        selected_date = request.form.get("date")
        today = datetime.today().strftime("%Y-%m-%d")
        
        if selected_date:
            if selected_date > today:
                error_message = "Date cannot be in the future!"
            elif selected_date < "1995-06-16":
                error_message = "APOD images start from June 16, 1995."
            else:
                apod_data = get_apod(selected_date)

    return render_template("history.html", apod=apod_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
