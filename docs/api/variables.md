# WeFact API Variables Quick Reference

This guide maps the API values to English enum names for easier development.

## Import

```python
from wefact.enums import (
    PricePeriod,
    CommunicationMethod,
    PaymentMethod,
    InvoiceStatus,
    QuoteStatus,
    TaskStatus,
    BoolInt,
    YesNo,
    VatCalculation,
    Gender,
    InvoiceSubStatus,
    PeriodicType,
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
    PricePeriod=PricePeriod.MONTHLY
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
    CommunicationMethod=CommunicationMethod.PHONE
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

## Boolean 0/1 Values (BoolInt)

Used for parameters that accept "0" or "1" as boolean strings.

| Enum Name | Value | English |
|-----------|-------|---------|
| `NO` / `FALSE` | `"0"` | No |
| `YES` / `TRUE` | `"1"` | Yes |

**Example:**
```python
client.invoices.create(
    DebtorCode="DB10001",
    IgnoreDiscount=BoolInt.YES,
    InvoiceLines=[...]
)
```

## Yes/No Values (YesNo)

Used for parameters that accept "yes" or "no".

| Enum Name | Value | English |
|-----------|-------|---------|
| `NO` | `"no"` | No |
| `YES` | `"yes"` | Yes |

**Example:**
```python
client.invoices.create(
    DebtorCode="DB10001",
    UseProductInventory=YesNo.YES,
    InvoiceLines=[...]
)
```

## VAT Calculation (VatCalculation)

Price calculation method for VAT.

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `EXCLUSIVE` / `EXCL` | `"excl"` | Exclusief BTW | Exclusive of VAT |
| `INCLUSIVE` / `INCL` | `"incl"` | Inclusief BTW | Inclusive of VAT |

**Example:**
```python
client.invoices.create(
    DebtorCode="DB10001",
    VatCalcMethod=VatCalculation.EXCLUSIVE,
    InvoiceLines=[...]
)
```

## Gender (Gender)

Person or entity gender/title.

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `MALE` / `M` | `"m"` | Man | Male |
| `FEMALE` / `F` | `"f"` | Vrouw | Female |
| `DIVERSE` / `D` | `"d"` | Divers | Diverse |
| `FAMILY` / `FAM` | `"fam"` | Familie | Family |
| `UNKNOWN` / `U` | `"u"` | Onbekend | Unknown |

**Example:**
```python
client.debtors.create(
    CompanyName="ABC Corp",
    Sex=Gender.DIVERSE
)
```

## Invoice Sub-Status (InvoiceSubStatus)

Additional invoice status flags.

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `BLOCKED` | `"BLOCKED"` | Geblokkeerd | Blocked |
| `PAUSED` | `"PAUSED"` | Gepauzeerd | Paused |

**Example:**
```python
client.invoices.edit(
    Identifier="123",
    SubStatus=InvoiceSubStatus.PAUSED
)
```

## Periodic Type (PeriodicType)

Invoice line periodic billing type.

| Enum Name | Value | Dutch | English |
|-----------|-------|-------|---------|
| `ONCE` | `"once"` | Eenmalig | One-time |
| `PERIOD` | `"period"` | Periodiek | Periodic |

**Example:**
```python
client.invoices.create(
    DebtorCode="DB10001",
    InvoiceLines=[{
        'ProductCode': 'P0001',
        'PeriodicType': PeriodicType.PERIOD,
        'Periods': 1,
        'Periodic': PricePeriod.MONTHLY
    }]
)
```

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
