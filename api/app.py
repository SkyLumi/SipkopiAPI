from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

current_moisture = {
    "moisture": 0,
    "timestamp": datetime.now().isoformat()
}

current_setting = {
    "status_penyiraman_otomatis": "OFF",
    "batas_kelembaban": 20.0
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

@app.route('/setting', methods=['GET'])
def get_setting():
    return jsonify(current_setting)

@app.route('/setting', methods=['POST'])
def update_setting():
    data = request.get_json()
    
    if 'status_penyiraman_otomatis' not in data or 'batas_kelembaban' not in data:
        return jsonify({'error': 'Payload harus memiliki status_penyiraman_otomatis dan batas_kelembaban'}), 400
    
    current_setting['status_penyiraman_otomatis'] = data['status_penyiraman_otomatis']
    current_setting['batas_kelembaban'] = float(data['batas_kelembaban'])

    return jsonify({
        'message': 'Pengaturan berhasil diperbarui',
        'data': current_setting
    }), 200

if __name__ == '__main__':
    app.run(debug=False)
