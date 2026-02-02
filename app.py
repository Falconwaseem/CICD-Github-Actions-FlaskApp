
import os

from flask import Flask

app = Flask(__name__)

ENVIRONMENT = os.getenv("APP_ENV", "dev")

PORT = int(os.getenv("APP_PORT", 4000))

@app.route("/")

def home():

    if ENVIRONMENT == "live":

        return "Welcome to Live this is deployment is done on live"

    return "Welcome to Dev"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=PORT)
