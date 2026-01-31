import os
from flask import Flask

app = Flask(__name__)
ENVIRONMENT = os.getenv("APP_ENV", "dev")
PORT = int(os.getenv("APP_PORT", 4000))

@app.route("/")
def home():
    if ENVIRONMENT == "live":
        return f"Welcome to Live Environment! Version: {os.getenv('VERSION', '1.0')}"
    return f"Welcome to Dev Environment! WORKFLOW FIX TEST Version deployed and checkif ready to deploy on live: {os.getenv('VERSION', '1.0')}"

@app.route("/health")
def health():
    return {"status": "healthy", "environment": ENVIRONMENT, "port": PORT}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)