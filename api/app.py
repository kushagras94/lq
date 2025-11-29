from flask import Flask, jsonify

app = Flask(__name__)  # <-- this *name* matters; Vercel looks for `app`

@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask on Vercel"})
