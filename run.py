from flask import Flask, render_template, flash, redirect, request, jsonify
from landerdb import Connect
import json

app = Flask(__name__)
db = Connect("mediacenter.db", autosave = True)

@app.route("/<number>", methods=["POST", "GET"])
@app.route("/", methods=['GET', "POST"])
def index(number = None):
    if request.method == "POST":
        url = request.form['url']
        name = request.form['name']
        artist = request.form['artist']
        urlid = url.split("=")[1]
        if not db.find("youtube", {"videoid":urlid}):
            db.insert("youtube", {"videoid":urlid, "name":name, "artist":artist})
    
    songs = db.find("youtube", "all")
    if not songs:
        songs = []
    return render_template("index.html", songs=songs, jsSongs =json.dumps({"data":songs}), number = json.dumps({"number":number}))


@app.route("/add/<name>/<artist>/<link>")
def add(name, artist, link):
    pass


app.run(debug=True)
