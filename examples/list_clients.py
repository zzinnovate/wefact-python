# list_clients.py
# Lists debtors (clients) using the WeFact API wrapper.

import os
import sys
from dotenv import load_dotenv

# Ensure local package import works when running the example directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wefact import WeFact  # noqa: E402


def main():
    load_dotenv()
    api_key = os.getenv('API_KEY') or os.getenv('WEFACT_API_KEY')
    if not api_key:
        print("Error: API_KEY (or WEFACT_API_KEY) not found in .env")
        raise SystemExit(1)

    client = WeFact(api_key)

    try:
        result = client.debtors.list()
        debtors = result.get('debtors', [])
        if not debtors:
            print("No clients found.")
            return
        for d in debtors:
            code = d.get('DebtorCode') or d.get('Identifier')
            name = d.get('CompanyName') or d.get('SurName') or d.get('Initials')
            print(f"Client: {code} - {name}")
    except Exception as e:
        print(f"Request failed: {e}")
        raise SystemExit(2)


if __name__ == '__main__':
    main()
