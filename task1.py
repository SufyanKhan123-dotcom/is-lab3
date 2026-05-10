import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def display(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Prev Hash:", block.previous_hash)
            print("-" * 30)

# Test
bc = Blockchain()
bc.add_block("Block 1 Data")
bc.add_block("Block 2 Data")
bc.add_block("Block 3 Data")
bc.add_block("Block 4 Data")

bc.display()

# Modify a block
bc.chain[2].data = "Hacked Data"
bc.chain[2].hash = bc.chain[2].calculate_hash()

print("\nAfter Tampering:\n")
bc.display()