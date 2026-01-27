from flask import Flask, request, make_response, jsonify
import uuid
from collections import defaultdict

app = Flask(__name__)

# память сервера (для free-tier достаточно)
stats = defaultdict(set)

@app.route("/track")
def track():
    page = request.args.get("page", "unknown")

    reader_id = request.cookies.get("reader_id")
    if not reader_id:
        reader_id = str(uuid.uuid4())

    stats[page].add(reader_id)

    resp = make_response("", 204)
    resp.set_cookie("reader_id", reader_id, max_age=60*60*24*365)
    return resp


@app.route("/stats")
def get_stats():
    return jsonify({page: len(readers) for page, readers in stats.items()})


@app.route("/")
def home():
    return "MSPFA tracker is running"
