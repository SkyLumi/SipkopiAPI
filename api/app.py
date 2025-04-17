from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

current_moisture = {
    "moisture": 0,
    "timestamp": datetime.now().isoformat()
}

@app.route('/moisture', methods=['GET'])
def get_moisture():
    return jsonify(current_moisture)

@app.route('/moisture', methods=['POST'])
def update_moisture():
    data = request.get_json()
    if 'moisture' not in data:
        return jsonify({'error': 'Data kelembapan tidak ditemukan'}), 400
     
    current_moisture['moisture'] = data['moisture']
    current_moisture['timestamp'] = datetime.now().isoformat()
    return jsonify({'message': 'Kelembapan berhasil diperbarui', 'data': current_moisture}), 200

if __name__ == '__main__':
    app.run(debug=False)
