from typing import List
import requests

class DatasetLoader:
    def __init__(self, benign_url, malicious_url):
        # Encapsulation: Store inputs in the object's memory
        self.benign_url = benign_url
        self.malicious_url = malicious_url

    def download_malicious(self):
        print(f"[INFO] Downloading malicious data from {self.malicious_url}...")
        
        # Perform the HTTP request
        response = requests.get(self.malicious_url)
        
        # Check for HTTP errors (raise exception if 404/500)
        response.raise_for_status()
        
        # Return the raw text content
        return response.text

    def download_benign(self):
        print(f"[INFO] Downloading benign data from {self.benign_url}...")
        
        # Perform the HTTP request
        response = requests.get(self.benign_url)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        return response.text
