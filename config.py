import os

# Load API keys from environment variables
INFURA_URL = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/6f4d52e14a7a4415a19c8db2bbad5794")

# Blockchain configuration
BLOCKCHAIN_NAME = "Ethereum"
DEFAULT_BLOCK = "latest"

# File paths
PROCESSED_DATA_PATH = "data/processed_data.csv"
REPORTS_PATH = "reports/"
