import hashlib
from block import Block


class Blockchain:

    def __init__(self):                                                 # initialization
        self.chain = []                                                 # keeps all blocks
        self.current_data = []                                          # keeps all the completed transactions in the block
        self.nodes = set()                                              #
        self.construct_initial_block()                                  # constructing the initial block

    def construct_initial_block(self):
        self.construct_block(proof_no = 0, prev_hash = 0)

    def construct_block(self, proof_no, prev_hash):                     # constructing block
        block = Block(
            index = len(self.chain),                                    # length of chain
            proof_no = proof_no,                                        # proof variable produced during block creation
            prev_hash = prev_hash,                                      # hash of previous block
            data = self.current_data
        )

        self.current_data = []

        self.chain.append(block)
        return block

    @staticmethod                                                       # logical method inside blockchain class
    def check_validity(block, prev_block):                              # checking whether hash of every block is correct
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not Blockchain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    def new_data(self, sender, recipient, quantity):                    # adding data of transaction to a block
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })

        return True

    def proof_of_work(self, last_proof):                                # a consensus algorithm
        proof_no = 0
        while Blockchain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):                             # a static method to verify whether hash of last proof and proof contains 4 leading zeros
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):                                             # returns current block in the chain
        return self.chain[-1]

    def block_mining(self, details_miner):                              # creating new block in the node

        self.new_data(
            sender = "0",
            receiver = details_miner,
            quantity = 1,
        )

        last_block = self.latest_block

        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)

        return vars(block)

    def create_node(self, address):                                     # creating node to mine from
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):                                # getting block
        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp = block_data['timestamp']
        )

