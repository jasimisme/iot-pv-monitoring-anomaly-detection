# mqtt/mqtt_client.py

import json
from datetime import datetime

import paho.mqtt.client as mqtt

from config import Config
from database.queries import (
    insert_telemetry
)


# =====================================================
# MQTT Callback: Connected
# =====================================================

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to MQTT Broker.")

        client.subscribe(Config.MQTT_TOPIC)

        print(f"Subscribed to topic: {Config.MQTT_TOPIC}")

    else:

        print(f"Failed to connect. Return code = {rc}")


# =====================================================
# MQTT Callback: Message Received
# =====================================================

def on_message(client, userdata, msg):

    try:

        # =============================================
        # Decode MQTT Payload
        # =============================================

        payload = msg.payload.decode("utf-8")

        data = json.loads(payload)

        print("Telemetry received:")
        print(data)


        # =============================================
        # Extract Telemetry Data
        # =============================================

        voltage = data["voltage"]

        current = data["current"]

        temperature = data["temperature"]

        irradiance = data["irradiance"]

        timestamp = data.get(
            "timestamp",
            datetime.now().isoformat()
        )


        # =============================================
        # Save to SQLite Database
        # =============================================

        insert_telemetry(
            voltage=voltage,
            current=current,
            temperature=temperature,
            irradiance=irradiance,
            timestamp=timestamp
        )

        print("Telemetry saved to database.")


    except Exception as e:

        print(f"MQTT message processing error: {e}")


# =====================================================
# Create MQTT Client
# =====================================================

def create_mqtt_client():

    client = mqtt.Client()

    client.on_connect = on_connect

    client.on_message = on_message

    return client


# =====================================================
# Start MQTT Listener
# =====================================================

def start_mqtt_listener():

    client = create_mqtt_client()

    client.connect(
        Config.MQTT_BROKER,
        Config.MQTT_PORT,
        Config.MQTT_KEEPALIVE
    )

    print("Starting MQTT listener...")

    client.loop_forever()


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    start_mqtt_listener()