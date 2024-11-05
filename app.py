from flask import Flask, jsonify, request, render_template
import hashlib, json, time, base64, binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

app = Flask(__name__)

# Encryption function using AES
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return cipher.nonce + tag + ciphertext

# Decryption function
def decrypt_data(encrypted_data, key):
    nonce, tag, ciphertext = encrypted_data[:16], encrypted_data[16:32], encrypted_data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

# Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # The encrypted data (name and phone number)
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_content.encode('utf-8')).hexdigest()

# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), {"name": "BASE BLOCK", "phone": "0000000000"}, "0")
        self.chain.append(genesis_block)

    def add_block(self, data, encryption_key):
        encrypted_data = {
            "name": base64.b64encode(encrypt_data(data['name'], encryption_key)).decode('utf-8'),
            "phone": base64.b64encode(encrypt_data(data['phone'], encryption_key)).decode('utf-8')
        }
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), encrypted_data, last_block.hash)
        self.chain.append(new_block)

# Create blockchain instance and key
my_blockchain = Blockchain()
encryption_key = get_random_bytes(16)

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.json
    my_blockchain.add_block(data, encryption_key)
    return jsonify({"message": "Contact added successfully"})

@app.route('/view_blockchain', methods=['GET'])
def view_blockchain():
    blockchain_with_decrypted_data = []
    for block in my_blockchain.chain:
        try:
            decrypted_data = {
                "name": decrypt_data(base64.b64decode(block.data["name"]), encryption_key),
                "phone": decrypt_data(base64.b64decode(block.data["phone"]), encryption_key)
            }
        except (binascii.Error, ValueError):
            decrypted_data = {"name": "Decryption failed", "phone": "Decryption failed"}

        blockchain_with_decrypted_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "decrypted_data": decrypted_data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        })
    return jsonify(blockchain_with_decrypted_data)

if __name__ == "__main__":
    app.run(debug=True)
