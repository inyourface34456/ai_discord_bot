import threading
from flask import Flask

app = Flask("")

@app.route("/")
def index():
    return "OK"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    keep_alive_thread = threading.Thread(target=run)
    keep_alive_thread.start()