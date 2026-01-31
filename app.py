from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'code': 200
    })

@app.route('/api/version')
def version():
    return jsonify({
        'version': '1.0.0',
        'app': 'Flask Demo'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
