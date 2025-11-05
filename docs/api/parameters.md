# WeFact API Parameters Reference

This document lists all available parameters for each WeFact API endpoint. Parameters marked with ⭐ are **required**.

## Table of Contents

- [Invoices](#invoices)
- [Debtors (Customers)](#debtors-customers)
- [Products](#products)
- [Subscriptions](#subscriptions)
- [Quotes](#quotes)
- [Creditors](#creditors)
- [Groups](#groups)
- [Cost Categories](#cost-categories)

---

## Invoices

### Create/Edit Invoice

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `Debtor` / `DebtorCode` | int / string | Customer ID or customer code |
| ⭐ `InvoiceLines` | array | Invoice lines (see below) - minimum 1 required |
| `InvoiceCode` | string | Invoice number (auto-generated if not provided) |
| `ExtraClientContactId` | int | Extra contact person ID |
| `Date` | date | Invoice date |
| `Term` | int | Payment term in days |
| `AmountPaid` | float | Amount already paid |
| **`Discount`** | **float** | **Discount on total invoice (percentage 0-100)** |
| **`IgnoreDiscount`** | **'0' or '1'** | **Ignore discount module (0=no, 1=yes). Default: 0** |
| `UseProductInventory` | 'yes' / 'no' | Update inventory. Default: yes |
| `VatCalcMethod` | 'excl' / 'incl' | Calculate VAT based on excl/incl. Default: admin setting |
| `ReferenceNumber` | string | Reference number |
| `CompanyName` | string | Customer: company name |
| `Initials` | string | Customer: first name |
| `SurName` | string | Customer: last name |
| `Sex` | 'm', 'f', 'd', 'fam', 'u' | Customer: gender. Default: 'm' |
| `Address` | string | Customer: address |
| `ZipCode` | string | Customer: postal code |
| `City` | string | Customer: city |
| `Country` | string | Customer: country (see variables list) |
| `EmailAddress` | string | Customer: email address |
| `InvoiceMethod` | int | Invoice sending method (see variables list) |
| `SentDate` | datetime | Invoice sent date |
| `Sent` | int | Number of times sent. Default: 0 |
| `LanguageCode` | string | Template language. Empty = default |
| `Authorisation` | 'yes' / 'no' | Direct debit. Default: customer preference |
| `PaymentMethod` | string | Payment method (see variables list) |
| `PayDate` | date | Payment date |
| `TransactionID` | string | Transaction ID of (online) payment |
| `Description` | string | Invoice description |
| `Comment` | text | Internal note |
| `Status` | int | Invoice status (see variables list). Default: 0 (draft) |
| `SubStatus` | string | "BLOCKED" to block draft, "PAUSED" to pause payment process |
| `CustomFields` | array | Custom fields (key=field code, value=value) |
| `AccountingCostCentre` | string | Cost center code (if activated) |
| `AccountingProject` | string | Project code (if activated) |

### Invoice Lines (InvoiceLines array)

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | int | Line ID (for editing existing lines) |
| `Date` | date | Date. Default: today |
| `Number` | float | Quantity. Default: 1 |
| `NumberSuffix` | string | Unit (e.g., "Kg") |
| `ProductCode` | string | Product code (auto-fills other fields) |
| `Description` | string | Description |
| `PriceExcl` | float | Price per unit (excl. VAT) |
| **`DiscountPercentage`** | **float** | **Line discount (percentage 0-100)** |
| **`DiscountPercentageType`** | **'line' / 'subscription'** | **Discount type (line only or also subscription)** |
| `TaxCode` | string | VAT code (found in VAT settings) |
| `StartDate` | date | Period start date |
| `EndDate` | date | Period end date (only if PeriodicType is 'once') |
| `PeriodicType` | 'once' / 'period' | Recurring billing? Default: 'once' |
| `Periods` | int | Invoice every: number of periods |
| `Periodic` | string | Invoice every: unit (see variables list) |
| `AccountingCostCentre` | string | Cost center code (if activated) |
| `AccountingProject` | string | Project code (if activated) |

**Note:** If `ProductCode` is provided, it auto-fills: `Description`, `PriceExcl`, `TaxCode`, `PeriodicType`, `Periods`, `Periodic`, and `StartDate`.

---

## Debtors (Customers)

### Create/Edit Debtor

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `CompanyName` / `SurName` | string | Company name OR last name (one required) |
| `DebtorCode` | string | Customer number (auto-generated if not provided) |
| `CompanyNumber` | string | Chamber of Commerce number |
| `TaxNumber` | string | VAT number |
| `Sex` | 'm', 'f', 'd', 'fam', 'u' | Gender. Default: 'm' |
| `Initials` | string | First name |
| `SurName` | string | Last name |
| `Address` | string | Address |
| `ZipCode` | string | Postal code |
| `City` | string | City |
| `Country` | string | Country (see variables list) |
| `EmailAddress` | string | Email address |
| `PhoneNumber` | string | Phone number |
| `MobileNumber` | string | Mobile number |
| `FaxNumber` | string | Fax number |
| `Comment` | text | Comment / note |
| `InvoiceMethod` | int | Invoice sending method. Default: 0 (email) |
| `DirectDebitApplyTo` | 'none', 'invoices', 'subscriptions', 'all' | Direct debit. Default: 'none' |
| `MandateID` | string | Mandate reference |
| `MandateDate` | date | Signature date. Default: today |
| `AccountNumber` | string | Bank account (IBAN) |
| `AccountName` | string | Account holder |
| `AccountBank` | string | Bank name |
| `AccountCity` | string | Bank city |
| `AccountBIC` | string | BIC code |
| `Mailing` | 'yes', 'no', 'unsubscribed' | Receive mailings |
| `InvoiceTerm` | int | Custom payment term |
| `PeriodicInvoiceDays` | '-1' / int | -1 uses default settings |
| `PaymentMail` | '-1' / int | -1 uses default settings |
| `LanguageCode` | string | Template language. Empty = default |
| `Currency` | string | Currency (see variables list) |
| `CustomTaxCode` | string | Custom VAT code. Empty = not custom |
| `ReminderEmailAddress` | string | Custom email for reminders |
| `Groups` | array | Array of customer group IDs or empty string |
| `CustomFields` | array | Custom fields (key=field code, value=value) |

---

## Products

### Create/Edit Product

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `ProductName` | string | Product name |
| ⭐ `ProductKeyPhrase` | string | Description on invoice |
| ⭐ `PriceExcl` | float | Price per unit (excl. VAT) |
| `ProductCode` | string | Product number (auto-generated if not provided) |
| `ProductDescription` | string | Extended (internal) description |
| `NumberSuffix` | string | Unit (e.g., "Kg") |
| `Barcode` | string | Barcode |
| `PricePeriod` | string | Subscription period (see variables list). Default: '' (no subscription) |
| `TaxCode` | string | VAT code |
| `AccountingCostCentre` | string | Cost center code (if activated) |
| `AccountingProject` | string | Project code (if activated) |
| `Groups` | array | Array of product group IDs or empty string |
| `ProductInventory` | array | Inventory settings (see below) |

### Product Inventory Settings

| Parameter | Type | Description |
|-----------|------|-------------|
| `IsProductInventoryEnabled` | 'yes' / 'no' | Update inventory. Default: yes |
| `TotalStock` | float | Quantity in stock |
| `StockWarningThreshold` | string | Warning threshold (empty for default) |
| `SupplierIds` | array | Array of supplier IDs or empty string |
| `WarehouseID` | int | Warehouse location |

---

## Subscriptions

### Create/Edit Subscription

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `Debtor` / `DebtorCode` | int / string | Customer ID or customer code |
| ⭐ `Subscription` | array | Subscription details (see below) |

### Subscription Details (Subscription array)

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `ProductCode` | string | Product code (if empty, Description/PriceExcl/Periodic required) |
| `Number` | float | Quantity. Default: 1 |
| `NumberSuffix` | string | Unit (e.g., "Kg") |
| `Description` | string | Description |
| `PriceExcl` | float | Price per unit (excl. VAT) |
| `TaxCode` | string | VAT code |
| **`DiscountPercentage`** | **float** | **Subscription discount (percentage 0-100)** |
| `Periods` | int | Invoice every: number of periods |
| `Periodic` | string | Invoice every: unit (see variables list) |
| `StartDate` | date | Period start date |
| `NextDate` | date | Next invoice date (only if 'invoice in advance' = 0) |
| `TerminationDate` | date | Cancellation date |
| `TerminateAfter` | int | Number of times to invoice. 0 = indefinite |
| `Comment` | text | Internal note |
| `AccountingCostCentre` | string | Cost center code (if activated) |
| `AccountingProject` | string | Project code (if activated) |
| `DirectDebit` | 'client', 'yes', 'no' | Direct debit. Default: 'client' (use customer setting) |

**Note:** Provide EITHER `TerminateAfter` OR `TerminationDate`, not both. `TerminateAfter` includes past invoices.

---

## Quotes

Quotes use the same parameters as [Invoices](#invoices), but with:
- Controller: `pricequote`
- `PriceQuoteLines` instead of `InvoiceLines`
- `PriceQuoteCode` instead of `InvoiceCode`

---

## Creditors

Creditors use similar parameters to [Debtors](#debtors-customers), but with:
- Controller: `creditor`
- `CreditorCode` instead of `DebtorCode`

---

## Groups

### Create/Edit Group

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `Type` | string | Group type: 'debtor', 'product', etc. |
| ⭐ `GroupName` | string | Group name |
| `Identifier` | int | Group ID (for editing) |

---

## Cost Categories

### Create/Edit Cost Category

| Parameter | Type | Description |
|-----------|------|-------------|
| ⭐ `Title` | string | Cost category title |
| `Identifier` | int | Cost category ID (for editing) |

---

## Discount Parameters Summary

| Resource | Parameter | Type | Description |
|----------|-----------|------|-------------|
| **Invoice** | `Discount` | float | Total invoice discount (0-100%) |
| **Invoice** | `IgnoreDiscount` | '0'/'1' | Ignore discount module |
| **Invoice Line** | `DiscountPercentage` | float | Line item discount (0-100%) |
| **Invoice Line** | `DiscountPercentageType` | 'line'/'subscription' | Discount scope |
| **Subscription** | `DiscountPercentage` | float | Subscription discount (0-100%) |
| **Quote** | Same as Invoice | | Uses PriceQuoteLines |

---

## Common Patterns

### Creating an Invoice with Discount

```python
from wefact import WeFact

client = WeFact(api_key='your-api-key')

result = client.invoices.create(
    DebtorCode='DB10001',
    Discount=10,  # 10% discount on total invoice
    InvoiceLines=[
        {
            'ProductCode': 'P0001',
            'Number': 2,
            'DiscountPercentage': 5,  # Additional 5% line discount
            'DiscountPercentageType': 'line'
        }
    ]
)
```

### Creating a Subscription with Discount

```python
result = client.subscriptions.create(
    DebtorCode='DB10001',
    Subscription={
        'ProductCode': 'P0001',
        'DiscountPercentage': 15,  # 15% recurring discount
        'Periodic': 'month'
    }
)
```

---

## Variable Lists

For enumerated values (countries, payment methods, etc.), refer to:
- [WeFact API Variables Documentation](https://developer.wefact.com/variables)

## Additional Resources

- [WeFact API Documentation](https://developer.wefact.com/)
- [API Errors](errors.md)
- [Endpoint Reference](endpoints.md)
