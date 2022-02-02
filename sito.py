from flask import Flask

app= Flask(__name__)

@app.route("/")

def Hello_World():
    return f"<p>Hello world!<p>"