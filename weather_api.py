from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")
stations = pd.read_csv("data_small/stations.txt", skiprows=17)

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def weather(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}

# @app.route("/api/v1/<word>")
# def api(word):
#     definition = df.loc[df["word"]==word]["definition"].squeeze()
#     return {"word": word, "definition": definition}


app.run(debug=True)