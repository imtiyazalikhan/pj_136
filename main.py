import pandas as pd
from flask import Flask, jsonify, request


#%matplotlib inline

df = pd.read_csv("star_with_gravity.csv")
df.head()

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/")
def index():
    name = request.arge.get("Star_name")
    star_data = next(item for item in data if item["Star_name"] == name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()