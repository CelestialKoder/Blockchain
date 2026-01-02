# Block Structure

Each block in the blockchain is an object of the Block class and contains the following components:

index  
This shows the position of the block in the blockchain.

timestamp  
This records the exact time the block was created.

data  
This holds the payload of the block, such as transaction data or messages.

previous_hash  
This keeps the hash of the previous block, creating a cryptographic link between blocks.

nonce  
This is a number that increases during mining to meet the Proof-of-Work condition.

hash  
This is the SHA-256 hash of the block's contents, calculated using all the above fields.

The hash is computed as:SHA256(index + timestamp + data + previous_hash + nonce)

# How validation logic detects tampering

Blockchain integrity is verified using the is_valid() method.

The validation logic checks two key conditions for every block, except the genesis block:

First(current block): 

The stored hash of latest block is recalculated and compared with its current contents.

If the data, nonce, or any field is changed, the recalculated hash will not match.

This makes the block invalid.

Second(Chain):

Each block’s previous_hash must exactly match the hash of the previous block.

If a block is altered, all subsequent blocks will have broken links.

If either condition fails, the blockchain is declared invalid.Therefore it effectively detects tampering.

#  Proof-of-Work approach

This blockchain uses a simplified Proof-of-Work method.

Mining Process

A difficulty level is set (e.g., difficulty = 2).

A valid block hash must start with a specific number of leading zeros:("0"*difficulty)

How Mining Works

A new block is created with an initial nonce value.

The block's hash is calculated.

If the hash doesn't meet the difficulty requirement, the nonce is increased.

The hash is recalculated.

This process continues until a valid hash is found.

This method makes block creation costly in terms of computing power, which prevents instant block generation .Thus,proving real world behaviour of PoW
