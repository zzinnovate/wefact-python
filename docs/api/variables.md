# WeFact API Variables Quick Reference

This guide maps the Dutch API values to English enum names for easier development.

## Import

```python
from wefact.enums import (
    PricePeriod,
    CommunicationMethod,
    PaymentMethod,
    InvoiceStatus,
    QuoteStatus,
    TaskStatus,
    get_enum_value,
)
```

## Price Periods (PricePeriod)

Used for product subscriptions.

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `NONE` / `""` | `""` | Geen abonnement | No subscription |
| `DAILY` / `DAY` | `"d"` | Dag | Day |
| `WEEKLY` / `WEEK` | `"w"` | Week | Week |
| `MONTHLY` / `MONTH` | `"m"` | Maand | Month |
| `QUARTERLY` / `QUARTER` | `"k"` | Kwartaal | Quarter |
| `HALF_YEARLY` / `HALF_YEAR` | `"h"` | Halfjaar | Half year |
| `YEARLY` / `YEAR` | `"j"` | Jaar | Year |
| `BIANNUAL` / `TWO_YEARS` | `"t"` | Twee jaar | Two years |

**Example:**
```python
client.products.create(
    ProductName="Hosting",
    PricePeriod=PricePeriod.MONTHLY.value  # 'm'
)
```

## Communication Methods (CommunicationMethod)

Used for interactions.

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `PHONE` | `"phone"` | Contact via telefoon | Phone |
| `WHATSAPP` | `"whatsapp"` | Contact via Whatsapp | WhatsApp |
| `EMAIL` | `"email"` | Contact via e-mail | Email |
| `POST` / `MAIL` | `"post"` | Contact per post | Mail |
| `IN_PERSON` / `FACE_TO_FACE` | `"in_person"` | Persoonlijk contact | In person |

**Example:**
```python
client.interactions.create(
    DebtorId=1,
    Description="Follow-up call",
    CommunicationMethod=CommunicationMethod.PHONE.value
)
```

## Payment Methods (PaymentMethod)

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `WIRE` / `BANK_TRANSFER` | `"wire"` | Bankoverschrijving | Bank transfer |
| `CASH` | `"cash"` | Contante betaling | Cash |
| `CARD` | `"card"` | Betaling via pin | Card/Pin |
| `AUTH` / `DIRECT_DEBIT` | `"auth"` | Automatische incasso | Direct debit |
| `ACCOUNTING` | `"accounting"` | Via boekhoudpakket | Via accounting |
| `VARIOUS` | `"various"` | Verschillende betaalmethoden | Various |
| `PAYPAL` | `"paypal"` | PayPal | PayPal |
| `IDEAL` | `"ideal"` | iDEAL | iDEAL |
| `QRCODE` | `"qrcode"` | QR Code | QR Code |
| `OTHER` | `"other"` | Online betaalmethode | Other online |

## Invoice Statuses (InvoiceStatus)

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `CONCEPT` / `DRAFT` | `"0"` | Concept factuur | Draft |
| `SENT` | `"2"` | Verzonden | Sent |
| `PARTIALLY_PAID` | `"3"` | Deels betaald | Partially paid |
| `PAID` | `"4"` | Betaald | Paid |
| `CREDIT` | `"8"` | Creditfactuur | Credit |
| `EXPIRED` | `"9"` | Vervallen | Expired |

## Quote Statuses (QuoteStatus)

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `CONCEPT` / `DRAFT` | `"0"` | Concept offerte | Draft |
| `SENT` | `"2"` | Verzonden | Sent |
| `ACCEPTED` | `"3"` | Geaccepteerd | Accepted |
| `INVOICE_CREATED` | `"4"` | Factuur aangemaakt | Invoice created |
| `DECLINED` / `REJECTED` | `"8"` | Geweigerd | Declined |

## Task Statuses (TaskStatus)

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `OPEN` | `"open"` | Open | Open |
| `IN_PROGRESS` | `"in_progress"` | In uitvoering | In progress |
| `COMPLETED` / `DONE` | `"completed"` | Voltooid | Completed |

## Helper Functions

### get_enum_value()

Convert from English name to API value (flexible, case-insensitive):

```python
from wefact.enums import get_enum_value, PricePeriod

# All of these work:
get_enum_value(PricePeriod, 'MONTHLY')   # Returns 'm'
get_enum_value(PricePeriod, 'monthly')   # Returns 'm'
get_enum_value(PricePeriod, 'MONTH')     # Returns 'm'
get_enum_value(PricePeriod, 'm')         # Returns 'm'
```

### get_enum_name()

Convert from API value to English name:

```python
from wefact.enums import get_enum_name, PricePeriod

get_enum_name(PricePeriod, 'm')  # Returns 'MONTHLY'
```

## Benefits

✅ **No more guessing**: Clear, English names instead of `'m'`, `'k'`, `'j'`  
✅ **IDE autocomplete**: See all available options as you type  
✅ **Type safety**: Enum validation catches typos  
✅ **Self-documenting**: Code explains itself  
✅ **Flexible**: Use English names or original Dutch values

## Complete Example

```python
from wefact import WeFact
from wefact.enums import PricePeriod, CommunicationMethod, TaskStatus

client = WeFact(api_key="your_key")

# Create monthly subscription product
product = client.products.create(
    ProductName="Premium Support",
    ProductKeyPhrase="premium-support",
    PriceExcl=49.99,
    PricePeriod=PricePeriod.MONTHLY.value,  # Clear!
    TaxPercentage=21.0
)

# Log phone interaction
interaction = client.interactions.create(
    AssigneeId=1,
    DebtorId=1,
    Description="Discussed subscription renewal",
    CommunicationMethod=CommunicationMethod.PHONE.value  # Clear!
)

# Create task
task = client.tasks.create(
    Title="Follow up with customer",
    Status=TaskStatus.OPEN.value  # Clear!
)
```
