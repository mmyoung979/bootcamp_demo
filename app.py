import os
from flask import Flask, request
import requests

app = Flask(__name__)
AUTH = f"api_key={os.environ.get('api_key')}"

@app.route("/", methods=["GET", "POST", "PATCH", "DELETE"])
def cats():
    if request.method == "GET":
        limit = request.args.get("limit", 1)
        url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&{AUTH}"
        response = requests.get(url).json()
        return [cat["url"] for cat in response]
    return {"message": f"{request.method} request"}
