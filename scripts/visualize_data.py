import pandas as pd
import matplotlib.pyplot as plt
from config import PROCESSED_DATA_PATH, REPORTS_PATH

def visualize_transaction_volume(data):
    plt.hist(data['value'], bins=50, alpha=0.7)
    plt.title("Transaction Volume Distribution")
    plt.xlabel("Ether")
    plt.ylabel("Frequency")
    output_path = f"{REPORTS_PATH}transaction_volume.png"
    plt.savefig(output_path)
    print(f"Transaction volume chart saved to {output_path}.")
