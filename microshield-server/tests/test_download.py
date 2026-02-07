from edge_ids.dataset import DatasetLoader

# Real URLs for testing
# Note: Tranco list is a ZIP file, but for now we test connectivity.
tranco_url = "https://tranco-list.eu/top-1m.csv.zip"
urlhaus_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"

print("--- START TEST ---")

# 1. Object Instantiation (calls __init__)
print("[INFO] Initializing Loader...")
loader = DatasetLoader(tranco_url, urlhaus_url)

# 2. Test Download Malicious
print("[INFO] Attempting to download malicious data...")
malicious_data = loader.download_malicious()

# Print the first 500 characters to verify content
print("[SUCCESS] Download complete! Preview of the data:")
print(malicious_data[:500])

print("--- END TEST ---")
