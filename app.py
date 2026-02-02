
import os

from flask import Flask

app = Flask(__name__)

ENVIRONMENT = os.getenv("APP_ENV", "dev")

PORT = int(os.getenv("APP_PORT", 4000))

@app.route("/")

def home():

    if ENVIRONMENT == "live":

        return "Welcome to Live"

    return "Welcome to Dev this is new update"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=PORT)
