import time
import hashlib


class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce                  
        self.hash = self.calculate_hash()   

    def calculate_hash(self):
        block_string = (str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.nonce))
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.chain = [self.genesis_block()]
    def genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")
    def latest_block(self):
        return self.chain[-1]
    def mine_block(self, block):
        target = "0" * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
    def add_block(self, data):
        prev_block = self.latest_block()
        new_block = Block(index=len(self.chain),timestamp=time.time(),data=data,previous_hash=prev_block.hash)
        self.mine_block(new_block)         
        self.chain.append(new_block)        

        print(f"Block {new_block.index} added with hash {new_block.hash}")
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                print(f"Invalid hash at block {i}")
                return False
            elif current.previous_hash != previous.hash:
                print(f"Broken link between block {i-1} and {i}")
                return False
            return True


        
