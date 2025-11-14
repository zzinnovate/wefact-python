"""
Example: Using WeFact Enums

This example demonstrates how to use the WeFact enums to avoid
dealing with Dutch abbreviations and make your code more readable.
"""

from wefact import WeFact
from wefact.enums import (
    PricePeriod,
    CommunicationMethod,
    TaskStatus,
    InvoiceStatus,
    PaymentMethod,
    get_enum_value,
    get_enum_name,
)

# Initialize client
client = WeFact(api_key="your_api_key_here")

# ============================================================================
# Example 1: Creating a product with readable enum instead of 'm' or 'j'
# ============================================================================
print("=== Creating Product ===")
product = client.products.create(
    ProductName="Premium Hosting",
    ProductKeyPhrase="premium-hosting",
    PriceExcl=24.99,
    PricePeriod=PricePeriod.MONTHLY.value,  # Instead of 'm'
    TaxPercentage=21.0
)
print(f"Created product: {product['product']['ProductCode']}")
print(f"Billing period: {product['product']['PricePeriod']}")  # Returns 'm'

# You can also use the helper function to be even more flexible
annual_product = client.products.create(
    ProductName="Annual License",
    ProductKeyPhrase="annual-license",
    PriceExcl=99.99,
    PricePeriod=get_enum_value(PricePeriod, 'YEARLY'),  # Converts 'YEARLY' to 'j'
    TaxPercentage=21.0
)

# ============================================================================
# Example 2: Creating an interaction with readable communication method
# ============================================================================
print("\n=== Creating Interaction ===")
interaction = client.interactions.create(
    AssigneeId=1,
    DebtorId=1,
    Description="Follow-up call about subscription renewal",
    CommunicationMethod=CommunicationMethod.PHONE.value,
)
print(f"Created interaction via: {interaction['interaction']['CommunicationMethod']}")

# English aliases work too!
email_interaction = client.interactions.create(
    AssigneeId=1,
    DebtorId=1,
    Description="Sent renewal confirmation",
    CommunicationMethod=CommunicationMethod.EMAIL.value,
)

# ============================================================================
# Example 3: Using flexible enum value conversion
# ============================================================================
print("\n=== Flexible Enum Conversion ===")

# All of these work and return 'm':
print(get_enum_value(PricePeriod, 'MONTHLY'))    # 'm'
print(get_enum_value(PricePeriod, 'monthly'))    # 'm' (case-insensitive)
print(get_enum_value(PricePeriod, 'MONTH'))      # 'm'
print(get_enum_value(PricePeriod, 'm'))          # 'm' (already correct value)

# Get human-readable name from value
print(get_enum_name(PricePeriod, 'm'))           # 'MONTHLY'

# ============================================================================
# Example 4: Task creation with status
# ============================================================================
print("\n=== Creating Task ===")
task = client.tasks.create(
    Title="Review contract",
    Description="Annual contract review for customer",
    DebtorId=1,
    # Status defaults to 'open', but you can set it:
    # Status=TaskStatus.IN_PROGRESS.value
)
print(f"Task created with status: {task['task'].get('Status', 'open')}")

# ============================================================================
# Example 5: All available enums
# ============================================================================
print("\n=== Available Enums ===")
print(f"Price Periods: {[p.name for p in PricePeriod]}")
print(f"Communication Methods: {[c.name for c in CommunicationMethod]}")
print(f"Task Statuses: {[t.name for t in TaskStatus]}")
print(f"Invoice Statuses: {[i.name for i in InvoiceStatus]}")
print(f"Payment Methods: {[p.name for p in PaymentMethod]}")

