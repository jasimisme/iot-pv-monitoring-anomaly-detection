from flask import Flask, jsonify, request

from database.queries import (
    get_latest_telemetry,
    get_telemetry_history,
    get_anomaly_logs
)

app = Flask(__name__)


# =========================================================
# 1. GET /api/live
# =========================================================

@app.route("/api/live", methods=["GET"])
def get_live_data():

    try:

        data = get_latest_telemetry()

        if data is None:

            return jsonify({
                "error": "No telemetry data found"
            }), 404

        return jsonify(data), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================================================
# 2. GET /api/anomaly
# =========================================================

@app.route("/api/anomaly", methods=["GET"])
def get_latest_anomaly():

    try:

        logs = get_anomaly_logs(limit=1)

        if len(logs) == 0:

            return jsonify({
                "status": "normal",
                "confidence": 1.0,
                "timestamp": None
            }), 200

        latest = logs[0]

        response = {
            "status": latest["fault"],
            "confidence": latest["confidence"],
            "timestamp": latest["timestamp"]
        }

        return jsonify(response), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================================================
# 3. GET /api/history?limit=100
# =========================================================

@app.route("/api/history", methods=["GET"])
def get_history():

    try:

        limit = request.args.get(
            "limit",
            default=100,
            type=int
        )

        data = get_telemetry_history(limit)

        return jsonify(data), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================================================
# 4. GET /api/anomaly/logs
# =========================================================

@app.route("/api/anomaly/logs", methods=["GET"])
def get_anomaly_logs_route():

    try:

        limit = request.args.get(
            "limit",
            default=100,
            type=int
        )

        logs = get_anomaly_logs(limit)

        return jsonify(logs), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================================================
# 5. GET /api/health
# =========================================================

@app.route("/api/health", methods=["GET"])
def health_check():

    try:

        health_status = {
            "status": "ok",
            "mqtt": "connected",
            "database": "connected",
            "model": "not_loaded"
        }

        return jsonify(health_status), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )