import os
import requests
import time
import random
from src import config

# List of user agents to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"
]

def download_file(url: str, file_name: str, directory: str, max_retries: int = 5, retry_delay: float = 2.0):
    """
    Downloads a file from a URL and saves it with the specified name.
    Retries on 403 errors and rotates User-Agents.
    """
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file_name)

    if os.path.isfile(file_path):
        print(f"[INFO] File '{file_path}' already exists. Skipping download.")
        return file_path

    print(f"[INFO] Downloading: '{url}' -> '{file_path}'")
    retries = 0
    while retries < max_retries:
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            with requests.get(url, headers=headers, stream=True, timeout=30) as response:
                if response.status_code == 403:
                    print(f"[WARNING] 403 Forbidden. Retrying ({retries + 1}/{max_retries})...")
                    retries += 1
                    time.sleep(retry_delay)
                    continue
                response.raise_for_status()
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"[SUCCESS] Downloaded '{file_path}'")
            return file_path
        except requests.RequestException as e:
            print(f"[ERROR] Download failed: {e}. Retrying ({retries + 1}/{max_retries})...")
            retries += 1
            time.sleep(retry_delay)

    print(f"[FAILURE] Failed to download '{url}' after {max_retries} attempts.")
    raise RuntimeError(f"Failed to download: {url}")

def download_all_files():
    """
    Loops through all hospital URLs in config and downloads them.
    """
    for hospital in config.HOSPITALS:
        download_file(
            url=hospital["url"],
            file_name=hospital["file_name"],
            directory=config.DATA_RAW
        )
