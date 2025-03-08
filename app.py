from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    submitted_text = None
    if request.method == "POST":
        submitted_text = request.form.get["text"]
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
