import hashlib
import time

class Block:

    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index                                                  # position of block within the blockchain
        self.proof_no = proof_no                                            # number to track position of a new block
        self.prev_hash = prev_hash                                          # hash to previous block
        self.data = data                                                    # record of all completed transactions
        self.timestamp = timestamp or time.time()                           # time of transactions

    @property
    def calculate_hash(self):                                               # method to calculate hash of block
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)
        return hashlib.sha256(block_of_string.encode()).hexdigest()         # returning hash of block string using sha256

    def __repr__(self):                                                     # formal representation of block
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)