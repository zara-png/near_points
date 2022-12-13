import geopy.distance
import json
import math
from urllib.request import urlopen

from flask import Flask,render_template,jsonify
import requests

app = Flask(__name__)


# def map_coordinates():
#
#     url = "https://api.npoint.io/f26432e9e880999eeb1b"
#
#     response = urlopen(url)
#     data_json = json.loads(response.read())
#     new = []
#     features = data_json["features"]
#
#     for i in range(len(features)):
#         new.append(features[i]["geometry"]["coordinates"])
#
#     send = json.dumps(new)
#     return send


@app.route('/')
def home():

    url = "https://api.npoint.io/f26432e9e880999eeb1b"

    response = urlopen(url)
    data_json = json.loads(response.read())
    new = []
    features = data_json["features"]

    for i in range(len(features)):
        new.append(features[i]["geometry"]["coordinates"])
    red = []
    blue = []

    for a in range(0,len(new)):
        for b in range(a+1,len(new)):
            x1 = new[a][0]
            x2 = new[b][0]
            y1 = new[a][1]
            y2 = new[b][1]

            result = geopy.distance.distance((x1,y1), (x2,y2)).km

            if result < 30.00:
                if new[a] not in red:
                    if new[a] not in blue:
                        red.append(new[a])
                    else:
                        blue.remove(new[a])

                if new[b] not in red:
                    if new[b] not in blue:
                        red.append(new[b])
                    else:
                        blue.remove(new[b])

            else:
                if new[a] not in blue:
                    if new[a] not in red:
                        blue.append(new[a])
                    else:
                        pass

                if new[b] not in blue:
                    if new[b] not in red:
                        blue.append(new[b])
                    else:
                        pass

    return render_template('index.html',red=red,blue=blue)


if __name__ == "__main__":
    app.run(debug=True)