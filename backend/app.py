from flask import Flask, jsonify
import test_datos

app = Flask(__name__)

@app.route('/api/emergency-contacts')
def emergency_contacts():
    return jsonify(test_datos.emergency-contacts)

# ... (continuación del código anterior)

@app.route('/api/model-config')
def model_config():
    return jsonify(test_datos.model_config)

@app.route('/api/sensor-settings')
def sensor_settings():
    return jsonify(test_datos.sensor_settings)

@app.route('/api/notification-preferences')
def notification_preferences():
    return jsonify(test_datos.notification_preferences)

@app.route('/api/users')
def users():
    return jsonify(test_datos.users)

@app.route('/api/realtime-accidents')
def realtime_accidents():
    return jsonify(test_datos.realtime_accidents)

@app.route('/api/system-status')
def system_status():
    return jsonify(test_datos.system_status)

if __name__ == "__main__":
    app.run()
