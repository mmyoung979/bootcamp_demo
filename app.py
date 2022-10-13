# Python imports
import os

# Third party imports
from flask import Flask, request
import requests

# Global variables
app = Flask(__name__)
AUTH = f"api_key={os.environ.get('api_key')}"

@app.route("/", methods=["GET", "POST", "PATCH", "DELETE"])
def cats():
    if request.method == "GET":
        # How many links to retrieve
        limit = request.args.get("limit", 1)

        # API request URL
        url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&{AUTH}"

        # API results
        response = requests.get(url).json()

        # Parse and return API results
        html = ""
        for cat in response:
            url = cat["url"]
            html += f"<img src={url}></img>"
        return html
