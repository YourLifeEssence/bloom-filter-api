from flask import Flask, request, jsonify
from bloom_filter import BloomFilter, hash_md5, hash_sha1, hash_sha256

app = Flask(__name__)

bloom = BloomFilter(size=1000, hash_funcs=[hash_md5, hash_sha1])

@app.route('/init', methods=['POST'])
def init():
    global bloom
    data = request.get_json()

    size = data.get('size', 1000)
    hash_names = data.get('hash_functions', ['md5', 'sha1'])

    hash_map = {
        'md5': hash_md5,
        'sha1': hash_sha1,
        'sha256': hash_sha256
    }

    hash_funcs = [hash_map[name] for name in hash_names if name in hash_map]

    bloom = BloomFilter(size=size, hash_funcs=hash_funcs)
    return jsonify({'status': 'initialized', 'size': size, 'functions': hash_names})
@app.route('/insert', methods=['POST'])
def insert():
    key = request.json.get('key')
    bloom.insert(key)
    return jsonify({'status': 'inserted', 'key': key})
@app.route('/check', methods=['GET'])
def check():
    key = request.args.get('key')
    result = bloom.contains(key)
    return jsonify({'key': key, 'result': result})
@app.route('/', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)