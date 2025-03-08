from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
data_file = "submitted_data.json"

#Saving submitted data to a JSON File
def collect_data(data):
    if os.path.exists(data_file):
        #Adds data if the file exists
        with open(data_file, "r") as file:
            allData = json.load(file)
    else:
        allData = {"data":[] }

    allData["data"].append(data)

    with open(data_file, "w") as file:
        json.dump(allData, file, indent = 4)
@app.route("/", methods = ["GET", "POST"])
def home():
    submitted_text = None
    if request.method == "POST":
        submitted_text = request.form.get("user_input")
        if submitted_text:
            collect_data(submitted_text)
    return render_template("index.html", submitted_text = submitted_text)

if __name__ == "__main__":
    app.run(debug=True)
