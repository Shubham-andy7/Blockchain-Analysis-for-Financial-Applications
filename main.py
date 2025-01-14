from scripts.fetch_blockchain_data import fetch_block_data
from scripts.analyze_transactions import analyze_transactions
from scripts.visualize_data import visualize_transaction_volume

def main():
    print("Fetching data from the blockchain...")
    block_data = fetch_block_data()
    
    print("Analyzing transactions...")
    transaction_analysis = analyze_transactions(block_data)
    
    print("Visualizing results...")
    visualize_transaction_volume(transaction_analysis)
    
    print("Analysis completed. Check the reports folder for results!")

if __name__ == "__main__":
    main()
