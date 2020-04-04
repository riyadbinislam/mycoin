from blockchain import Blockchain

bchain = Blockchain()

print('***Mining mycoin about to start***')
print(bchain.chain)

last_block = bchain.latest_block
last_proof_no = last_block.proof_no
proof_no = bchain.proof_of_work(last_proof_no)

bchain.new_data(
    sender = "122",
    recipient = "sfsf sfsf",
    quantity = 10,
)


last_hash = last_block.calculate_hash
block = bchain.construct_block(proof_no, last_hash)

print("***Mining mycoin has been successful***")
print(bchain.chain)
