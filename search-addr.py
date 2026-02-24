import os
import requests
import json
import sys
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# --- Configuration from Environment Variables ---
# os.getenv('KEY', 'default_value') allows for local defaults
BASE_URL = os.getenv("JP_API_BASE_URL", "https://api.da.pf.japanpost.jp/api/v1")
TOKEN_URL = f"{BASE_URL}/j/token"
SEARCH_BASE_URL = f"{BASE_URL}/searchcode"

CLIENT_ID = os.getenv("JP_CLIENT_ID")
SECRET_KEY = os.getenv("JP_SECRET_KEY")

def get_jwt_token():
    # Basic check to ensure credentials exist
    if not CLIENT_ID or not SECRET_KEY:
        print("Error: Missing credentials in .env file.")
        return None

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "secret_key": SECRET_KEY
    }
    
    try:
        response = requests.post(TOKEN_URL, json=payload, timeout=10)
        response.raise_for_status()
        return response.json().get("token")
    except Exception as e:
        print(f"Auth Error: {e}")
        return None

def search_by_code(search_code, token):
    url = f"{SEARCH_BASE_URL}/{search_code}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code, response.json()
    except Exception as e:
        return 500, {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search-addr.py <zip_code>")
        sys.exit(1)

    input_code = sys.argv[1]
    token = get_jwt_token()
    
    if not token:
        sys.exit(1)

    status, data = search_by_code(input_code, token)

    if status == 200:
        addresses = data.get("addresses", [])
        if not addresses:
            print("No address found.")
        else:
            for addr in addresses:
                full_address = f"{addr['pref_name']}{addr['city_name']}{addr['town_name']}{addr['block_name'] or ''}"
                biz_info = f" ({addr['biz_name']})" if addr.get('biz_name') else ""
                print(f"[{addr['zip_code']}] {full_address}{biz_info}")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
