from flask import Flask, render_template, jsonify, request
from api import get_artsy_data
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/artist/<name>")
def get_artist(name):
    res = get_artsy_data(f"search?q={name}&size=10&type=artist")
    if res['_embedded']['results'] == []:
        return jsonify('')
    data = []
    for item in res['_embedded']['results']:
        name = item['title']
        thumbnail = item['_links']['thumbnail']['href']
        data.append({
            "name": name,
            "thumbnail": thumbnail,
            "id": item['_links']['self']['href'].split('/')[-1]
        })
    return jsonify(data)


@app.route("/api/artist/details/<artist_id>")
def get_artist_details(artist_id):
    artist = get_artsy_data(f"artists/{artist_id}")
    print(artist)
    if artist:
        return jsonify(artist)
    return jsonify({"error": "Artist details not found"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
