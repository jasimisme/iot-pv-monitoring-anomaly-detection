from database.db import connect_db


# =====================================================
# Insert Telemetry Data
# =====================================================

def insert_telemetry(
    voltage,
    current,
    temperature,
    irradiance,
    timestamp
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO telemetry (
        voltage,
        current,
        temperature,
        irradiance,
        timestamp
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        voltage,
        current,
        temperature,
        irradiance,
        timestamp
    ))

    conn.commit()

    conn.close()


# =====================================================
# Get Latest Telemetry
# =====================================================

def get_latest_telemetry():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM telemetry
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row is None:

        return None

    return dict(row)


# =====================================================
# Get Telemetry History
# =====================================================

def get_telemetry_history(limit=100):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM telemetry
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


# =====================================================
# Insert Anomaly Log
# =====================================================

def insert_anomaly_log(
    fault,
    confidence,
    timestamp
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO anomaly_logs (
        fault,
        confidence,
        timestamp
    )
    VALUES (?, ?, ?)
    """, (
        fault,
        confidence,
        timestamp
    ))

    conn.commit()

    conn.close()


# =====================================================
# Get Anomaly Logs
# =====================================================

def get_anomaly_logs(limit=100):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM anomaly_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]