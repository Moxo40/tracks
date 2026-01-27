from flask import Flask, request, make_response, jsonify
import uuid
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)

# page -> set(reader_id)
stats = defaultdict(set)

# лог событий (для будущего расширения)
events = []

@app.route("/track")
def track():
    page = request.args.get("page")
    if not page:
        return "page required", 400

    reader_id = request.cookies.get("reader_id")
    if not reader_id:
        reader_id = str(uuid.uuid4())

    stats[page].add(reader_id)
    events.append({
        "time": datetime.utcnow().isoformat(),
        "page": page,
        "reader": reader_id
    })

    resp = make_response("", 204)
    resp.set_cookie(
        "reader_id",
        reader_id,
        max_age=60 * 60 * 24 * 365,
        samesite="Lax"
    )
    return resp


@app.route("/stats")
def get_stats():
    # сортируем страницы как числа
    pages = sorted(stats.keys(), key=lambda x: int(x))

    base = len(stats[pages[0]]) if pages else 1

    result = []
    for p in pages:
        count = len(stats[p])
        percent = round((count / base) * 100, 1) if base else 0
        result.append({
            "page": int(p),
            "unique": count,
            "percent": percent
        })

    return jsonify({
        "total_readers": base,
        "pages": result
    })


@app.route("/")
def home():
    return "MSPFA tracker running"
