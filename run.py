from flask import Flask, render_template, flash, redirect, request, jsonify
from landerdb import Connect
import json

app = Flask(__name__)
db = Connect("mediacenter.db", autosave = True)

@app.route("/", methods=["POST", "GET"])
def index():
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
    return render_template("index.html", songs=songs, jsSongs =json.dumps({"data":songs}))



app.run(debug=True)
