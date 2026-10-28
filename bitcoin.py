import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")



try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin",
        headers={"Authorization": "Bearer KEY"}
    )
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException as e:
    sys.exit(f"Could not retrieve Bitcoin price: {e}")


print(f"${amount * price:,.4f}")
