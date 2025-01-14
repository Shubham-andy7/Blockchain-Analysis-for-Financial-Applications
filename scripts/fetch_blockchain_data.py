from web3 import Web3
from config import INFURA_URL, DEFAULT_BLOCK

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
print(INFURA_URL)
def fetch_block_data(block_number=DEFAULT_BLOCK):
    if not web3.is_connected():
        raise ConnectionError("Unable to connect to the Ethereum blockchain.")
    
    block = web3.eth.get_block(block_number, full_transactions=True)
    print(f"Fetched block {block['number']} with {len(block['transactions'])} transactions.")
    return block
