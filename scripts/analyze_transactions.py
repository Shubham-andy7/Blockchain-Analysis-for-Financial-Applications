import pandas as pd

def analyze_transactions(block):
    transactions = []
    for tx in block.transactions:
        transactions.append({
            "hash": tx.hash.hex(),
            "from": tx["from"],
            "to": tx.get("to", "Contract Creation"),
            "value": tx["value"] / 1e18,  # Convert wei to Ether
            "gas_price": tx["gasPrice"] / 1e9,  # Convert wei to Gwei
        })
    df = pd.DataFrame(transactions)
    df.to_csv("data/processed_data.csv", index=False)
    print("Transaction data saved to data/processed_data.csv.")
    return df
