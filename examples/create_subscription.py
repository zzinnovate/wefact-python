# create_subscription.py

from wefact import WeFact
from wefact.enums import PricePeriod

def create_subscription(api_key, debtor_code, product_code, description, price_excl, periodic, terminate_after):
    # Initialize the WeFact client
    client = WeFact(api_key)

    # Create the subscription
    subscription_data = {
        'DebtorCode': debtor_code,
        'ProductCode': product_code,
        'Description': description,
        'PriceExcl': price_excl,
        'Periodic': periodic,
        'TerminateAfter': terminate_after
    }

    response = client.subscriptions.create(**subscription_data)

    if response['status'] == 'success':
        print("Subscription created successfully:")
        print(response['subscription'])
    else:
        print("Failed to create subscription:")
        print(response['errors'])

if __name__ == "__main__":
    # Replace with your actual API key and subscription details
    API_KEY = 'your-api-key'
    DEBTOR_CODE = 'DB10000'
    PRODUCT_CODE = 'P0001'
    DESCRIPTION = 'Your product description'
    PRICE_EXCL = 100
    PERIODIC = PricePeriod.MONTHLY  # Use enum instead of 'month'
    TERMINATE_AFTER = 12

    create_subscription(API_KEY, DEBTOR_CODE, PRODUCT_CODE, DESCRIPTION, PRICE_EXCL, PERIODIC, TERMINATE_AFTER)