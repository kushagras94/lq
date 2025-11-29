from flask import Flask, jsonify

# Vercel looks specifically for this name: `app`
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask on Vercel!"})
