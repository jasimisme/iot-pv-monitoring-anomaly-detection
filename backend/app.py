from flask import Flask, jsonify, request

app = Flask(__name__)

# =========================================================
# Dummy in-memory data
# (sementara untuk testing awal)
# =========================================================

latest_sensor_data = {
    "voltage": 18.2,
    "current": 4.1,
    "temperature": 31.0,
    "irradiance": 840,
    "timestamp": "2026-05-26T10:30:00"
}

latest_anomaly = {
    "status": "normal",
    "confidence": 0.97,
    "timestamp": "2026-05-26T10:30:01"
}

sensor_history = [
    {
        "timestamp": "2026-05-26T10:00:00",
        "voltage": 18.1,
        "current": 4.0
    },
    {
        "timestamp": "2026-05-26T10:05:00",
        "voltage": 18.3,
        "current": 4.2
    }
]

anomaly_logs = [
    {
        "timestamp": "2026-05-26T09:12:00",
        "fault": "mismatch_fault"
    }
]

# =========================================================
# 1. GET /api/live
# =========================================================

@app.route("/api/live", methods=["GET"])
def get_live_data():

    try:
        return jsonify(latest_sensor_data), 200

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
        return jsonify(latest_anomaly), 200

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
        limit = request.args.get("limit", default=100, type=int)

        data = sensor_history[:limit]

        return jsonify(data), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# =========================================================
# 4. GET /api/anomaly/logs
# =========================================================

@app.route("/api/anomaly/logs", methods=["GET"])
def get_anomaly_logs():

    try:
        return jsonify(anomaly_logs), 200

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
            "model": "loaded"
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