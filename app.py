from flask import Flask, jsonify

app = Flask(__name__)
API_KEY = "AIajkdbaidvk16w787he1oehjl2"

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


@app.route('/api/health_v2')
def health_v2():
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
