import os


class Config:

    # =====================================================
    # Flask Server Configuration
    # =====================================================

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "pv-monitor-secret-key"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "True"
    ) == "True"

    HOST = os.getenv(
        "HOST",
        "0.0.0.0"
    )

    PORT = int(os.getenv(
        "PORT",
        5000
    ))


    # =====================================================
    # MQTT Configuration
    # =====================================================

    MQTT_BROKER = os.getenv(
        "MQTT_BROKER",
        "localhost"
    )

    MQTT_PORT = int(os.getenv(
        "MQTT_PORT",
        1883
    ))

    MQTT_TOPIC = os.getenv(
        "MQTT_TOPIC",
        "pv/telemetry"
    )

    MQTT_KEEPALIVE = int(os.getenv(
        "MQTT_KEEPALIVE",
        60
    ))


    # =====================================================
    # SQLite Database Configuration
    # =====================================================

    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "database/pv_monitor.db"
    )


    # =====================================================
    # AI Model Configuration
    # =====================================================

    MODEL_PATH = os.getenv(
        "MODEL_PATH",
        "ai/model.pkl"
    )


    # =====================================================
    # WebSocket Configuration
    # =====================================================

    SOCKET_ASYNC_MODE = os.getenv(
        "SOCKET_ASYNC_MODE",
        "threading"
    )


    # =====================================================
    # Telemetry Configuration
    # =====================================================

    DEFAULT_HISTORY_LIMIT = int(os.getenv(
        "DEFAULT_HISTORY_LIMIT",
        100
    ))


    # =====================================================
    # Logging Configuration
    # =====================================================

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    LOG_FILE = os.getenv(
        "LOG_FILE",
        "storage/backend.log"
    )