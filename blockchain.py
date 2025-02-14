import hashlib
import time
import json
from flask import Flask, request, jsonify

# Klasa që përfaqëson një bllok në blockchain
class Block:
    def __init__(self, index, previous_hash, data, difficulty):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.calculate_hash()  # Inicializojmë hash-in
        self.hash = self.mine_block()  # Minimi i bllokut

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self):
        """ Zbaton mekanizmin Proof of Work (PoW) duke kërkuar një hash me një numër të caktuar zerosh në fillim. """
        while self.hash[:self.difficulty] != "0" * self.difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        return self.hash

# Klasa që përfaqëson Blockchain-in
class Blockchain:
    def __init__(self):
        self.difficulty = 4  # Inicializimi i vështirësisë
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """ Krijon bllokun e parë (Genesis Block). """
        return Block(0, "0", "Genesis Block", self.difficulty)

    def add_block(self, data):
        """ Shton një bllok të ri në zinxhir. """
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data, self.difficulty)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        """ Verifikon integritetin e zinxhirit të blloqeve. """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_chain(self):
        """ Kthen të gjithë blockchain-in në format JSON. """
        return json.dumps([block.__dict__ for block in self.chain], indent=4)

# Inicializimi i blockchain-it
blockchain = Blockchain()

# Krijimi i API-së për të ndërvepruar me blockchain-in
app = Flask(__name__)

@app.route('/mine', methods=['POST'])
def mine_block():
    """ Endpoint për të shtuar një bllok të ri në blockchain. """
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "Data e bllokut nuk mund të jetë bosh!"}), 400

    new_block = blockchain.add_block(data)
    return jsonify({"message": "Blloku u minua me sukses!", "block": new_block.__dict__}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    """ Endpoint për të marrë zinxhirin e plotë të blloqeve. """
    return blockchain.get_chain()

@app.route('/validate', methods=['GET'])
def validate_chain():
    """ Endpoint për të verifikuar integritetin e zinxhirit. """
    valid = blockchain.is_chain_valid()
    return jsonify({"valid": valid})

if __name__ == '__main__':
    app.run(debug=True)
