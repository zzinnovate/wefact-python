# API Parameters Reference

Complete parameter documentation for all WeFact API resources.

## Invoices

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Debtor` | string | Customer ID (numeric string like "5") |
| `DebtorCode` | string | **Or** use customer code (e.g., "DB10000") |
| `InvoiceLines` | array | Array of line items (minimum 1 required) |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `InvoiceCode` | string | Invoice number (auto-generated if omitted) |
| `Date` | string | Invoice date (YYYY-MM-DD) |
| `Term` | int | Payment term in days |
| `Discount` | float | Total invoice discount (0-100%) |
| `Status` | int | Status: 0=Draft, 2=Sent, 4=Paid, etc. |
| ... | | (See full parameter list below) |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Invoice ID (numeric string like "5") |
| `InvoiceCode` | string | **Or** use invoice code (e.g., "INV10000") |

**Optional:** Same parameters as `create()` (except `Identifier`/`InvoiceCode` is required, not optional).

### All Invoice Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Invoice ID (for edit - see above) |
| `InvoiceCode` | string | Invoice number (auto-generated if omitted) |
| `ExtraClientContactId` | string | Extra contact person ID |
| `Date` | string | Invoice date (YYYY-MM-DD) |
| `Term` | int | Payment term in days |
| `AmountPaid` | float | Amount already paid |
| `Discount` | float | Total invoice discount (0-100%) |
| `IgnoreDiscount` | string | Ignore discount module: "0" (no) or "1" (yes) |
| `UseProductInventory` | string | Update inventory: "yes" or "no" |
| `VatCalcMethod` | string | VAT calculation: "excl" or "incl" |
| `ReferenceNumber` | string | Reference number |
| `CompanyName` | string | Override customer company name |
| `Initials` | string | Override customer first name |
| `SurName` | string | Override customer last name |
| `Sex` | string | Gender: "m", "f", "d", "fam", "u" |
| `Address` | string | Override customer address |
| `ZipCode` | string | Override customer postal code |
| `City` | string | Override customer city |
| `Country` | string | Override customer country code |
| `EmailAddress` | string | Override customer email |
| `InvoiceMethod` | int | Sending method (0=email, see variables) |
| `SentDate` | string | Invoice sent date (YYYY-MM-DD HH:MM:SS) |
| `Sent` | int | Number of times sent |
| `LanguageCode` | string | Template language code |
| `Authorisation` | string | Direct debit: "yes" or "no" |
| `PaymentMethod` | string | Payment method code |
| `PayDate` | string | Payment date (YYYY-MM-DD) |
| `TransactionID` | string | Transaction ID |
| `Description` | string | Invoice description |
| `Comment` | string | Internal note |
| `Status` | int | Status: 0=Draft, 2=Sent, 4=Paid, etc. |
| `SubStatus` | string | "BLOCKED" or "PAUSED" |
| `CustomFields` | array | Custom field values |
| `AccountingCostCentre` | string | Cost center code |
| `AccountingProject` | string | Project code |

### InvoiceLines Array

Each line item in the `InvoiceLines` array:

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Line ID (for editing existing lines) |
| `ProductCode` | string | Product code (auto-fills other fields) |
| `Description` | string | Line description |
| `PriceExcl` | float | Price per unit (excl. VAT) |
| `Number` | float | Quantity (default: 1) |
| `NumberSuffix` | string | Unit (e.g., "Kg", "hours") |
| `DiscountPercentage` | float | Line discount (0-100%) |
| `DiscountPercentageType` | string | "line" or "subscription" |
| `TaxCode` | string | VAT code |
| `Date` | string | Line date (YYYY-MM-DD) |
| `StartDate` | string | Period start (YYYY-MM-DD) |
| `EndDate` | string | Period end (YYYY-MM-DD) |
| `PeriodicType` | string | "once" or "period" |
| `Periods` | int | Invoice every X periods |
| `Periodic` | string | Period unit: "month", "year", etc. |
| `AccountingCostCentre` | string | Cost center code |
| `AccountingProject` | string | Project code |

!!! info "Auto-fill from ProductCode"
    When `ProductCode` is provided, it automatically fills: `Description`, `PriceExcl`, `TaxCode`, `PeriodicType`, `Periods`, `Periodic`, and `StartDate`.

---

## Credit Invoices

!!! info "Parameter Differences from Invoices"
    Credit invoices (purchase invoices) use similar parameters to regular invoices with these differences:
    
    - Use `CreditInvoiceCode` instead of `InvoiceCode`
    - Use `CreditInvoiceLines` instead of `InvoiceLines`
    - Use `Creditor` or `CreditorCode` instead of `Debtor` or `DebtorCode`
    
    Refer to the [Invoices](#invoices) section for parameter details.

---

## Debtors (Customers)

### create()

**Required (one of):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `CompanyName` | string | Company name |
| `SurName` | string | **Or** last name (individual) |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Debtor ID (numeric string) |
| `DebtorCode` | string | **Or** use debtor code (e.g., "DB10000") |

**Optional:** Same as `create()`.

### All Debtor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `DebtorCode` | string | Customer number (auto-generated if omitted) |
| `CompanyNumber` | string | Chamber of Commerce number |
| `TaxNumber` | string | VAT number |
| `Sex` | string | Gender: "m", "f", "d", "fam", "u" |
| `Initials` | string | First name |
| `Address` | string | Street address |
| `ZipCode` | string | Postal code |
| `City` | string | City |
| `Country` | string | Country code (ISO 3166-1 alpha-2) |
| `EmailAddress` | string | Email address |
| `PhoneNumber` | string | Phone number |
| `MobileNumber` | string | Mobile number |
| `FaxNumber` | string | Fax number |
| `Comment` | string | Internal note |
| `InvoiceMethod` | int | Sending method: 0=email, 1=post, 2=email+post |
| `DirectDebitApplyTo` | string | Direct debit: "none", "invoices", "subscriptions", "all" |
| `MandateID` | string | SEPA mandate reference |
| `MandateDate` | string | Mandate signature date (YYYY-MM-DD) |
| `AccountNumber` | string | Bank account (IBAN) |
| `AccountName` | string | Account holder name |
| `AccountBank` | string | Bank name |
| `AccountCity` | string | Bank city |
| `AccountBIC` | string | BIC/SWIFT code |
| `Mailing` | string | Receive mailings: "yes", "no", "unsubscribed" |
| `InvoiceTerm` | int | Custom payment term (days) |
| `PeriodicInvoiceDays` | int | Periodic invoice day (-1 = use default) |
| `PaymentMail` | int | Payment confirmation (-1 = use default) |
| `LanguageCode` | string | Template language code |
| `Currency` | string | Currency code (EUR, USD, etc.) |
| `CustomTaxCode` | string | Custom VAT code |
| `ReminderEmailAddress` | string | Alternative reminder email |
| `Groups` | array | Array of customer group IDs |
| `CustomFields` | array | Custom field values |

---

## Creditors (Suppliers)

### create()

**Required (one of):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `CompanyName` | string | Company name |
| `SurName` | string | **Or** last name (individual) |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Creditor ID (numeric string) |
| `CreditorCode` | string | **Or** use creditor code (e.g., "CD50000") |

**Optional:** Same as `create()`.

### All Creditor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `CreditorCode` | string | Creditor number (auto-generated if omitted) |
| `MyCustomerCode` | string | Your customer number with this supplier |
| `CompanyNumber` | string | Chamber of Commerce number |
| `TaxNumber` | string | VAT number |
| `Sex` | string | Gender: "m", "f", "d", "fam", "u" |
| `Initials` | string | First name |
| `Address` | string | Street address |
| `ZipCode` | string | Postal code |
| `City` | string | City |
| `Country` | string | Country code (ISO 3166-1 alpha-2) |
| `EmailAddress` | string | Email address |
| `PhoneNumber` | string | Phone number |
| `MobileNumber` | string | Mobile number |
| `FaxNumber` | string | Fax number |
| `Comment` | string | Internal note |
| `Authorisation` | string | Direct debit authorization: "yes" or "no" |
| `AccountNumber` | string | Bank account (IBAN) |
| `AccountName` | string | Account holder name |
| `AccountBank` | string | Bank name |
| `AccountCity` | string | Bank city |
| `AccountBIC` | string | BIC/SWIFT code |
| `InvoiceTerm` | int | Payment term (days) |
| `ProductInventory` | array | Product inventory settings (see below) |

### ProductInventory Array (Creditors)

| Parameter | Type | Description |
|-----------|------|-------------|
| `ProductIds` | array | Array of product IDs linked to this creditor |

---

## Products

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ProductName` | string | Product name |
| `ProductKeyPhrase` | string | Description shown on invoices |
| `PriceExcl` | float | Price per unit (excl. VAT) |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Product ID (numeric string) |
| `ProductCode` | string | **Or** use product code |

**Optional:** Same as `create()`.

### All Product Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ProductCode` | string | Product number (auto-generated if omitted) |
| `ProductDescription` | string | Extended internal description |
| `NumberSuffix` | string | Unit (e.g., "Kg", "hours") |
| `Barcode` | string | Product barcode |
| `PricePeriod` | string | Subscription period: "month", "year", etc. (empty = one-time) |
| `TaxCode` | string | VAT code |
| `AccountingCostCentre` | string | Cost center code |
| `AccountingProject` | string | Project code |
| `Groups` | array | Array of product group IDs |
| `ProductInventory` | array | Inventory settings (see below) |

### ProductInventory Array

| Parameter | Type | Description |
|-----------|------|-------------|
| `IsProductInventoryEnabled` | string | Track inventory: "yes" or "no" |
| `TotalStock` | float | Current stock quantity |
| `StockWarningThreshold` | string | Low stock warning level |
| `SupplierIds` | array | Array of supplier IDs |
| `WarehouseID` | string | Warehouse location ID |

---

## Subscriptions

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Debtor` | string | Customer ID (numeric string) |
| `DebtorCode` | string | **Or** customer code (e.g., "DB10000") |
| `Subscription` | array | Subscription details (see below) |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Subscription ID (numeric string) |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Subscription` | array | Subscription details to update |

### Subscription Array

**Required Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ProductCode` | string | Product code |
| `Description` | string | **Or** description (if no ProductCode) |
| `PriceExcl` | float | **And** price (if no ProductCode) |
| `Periodic` | string | **And** period unit (if no ProductCode) |

**Optional Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Number` | float | Quantity (default: 1) |
| `NumberSuffix` | string | Unit (e.g., "Kg") |
| `TaxCode` | string | VAT code |
| `DiscountPercentage` | float | Recurring discount (0-100%) |
| `Periods` | int | Invoice every X periods (default: 1) |
| `StartDate` | string | Period start date (YYYY-MM-DD) |
| `NextDate` | string | Next invoice date (YYYY-MM-DD) |
| `TerminationDate` | string | Cancellation date (YYYY-MM-DD) |
| `TerminateAfter` | int | Number of invoices (0 = indefinite) |
| `Comment` | string | Internal note |
| `AccountingCostCentre` | string | Cost center code |
| `AccountingProject` | string | Project code |
| `DirectDebit` | string | Direct debit: "client", "yes", "no" |

!!! warning "Termination Parameters"
    Use either `TerminationDate` or `TerminateAfter`, not both.

---

## Quotes

!!! info "Parameter Differences from Invoices"
    Quotes use the same parameters as [Invoices](#invoices) with these differences:
    
    - Use `PriceQuoteCode` instead of `InvoiceCode`
    - Use `PriceQuoteLines` instead of `InvoiceLines`

---

## Interactions

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `AssigneeId` | string | Employee ID assigned to this interaction |
| `Description` | string | Interaction description |
| `CommunicationMethod` | string | Contact method (see variables list) |

**Required (one of):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `DebtorId` | string | Customer ID |
| `CreditorId` | string | Supplier ID |
| `InvoiceId` | string | Invoice ID |
| `PriceQuoteId` | string | Quote ID |
| `CreditInvoiceId` | string | Credit invoice ID |
| `UnprocessedCreditInvoiceId` | string | Unprocessed credit invoice ID |
| `SubscriptionId` | string | Subscription ID |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Date` | string | Interaction date (YYYY-MM-DD) |
| `Hours` | string | Hour of interaction (HH) |
| `Minutes` | string | Minutes of interaction (MM) |
| `DebtorContactId` | string | Customer contact person ID |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Interaction ID (numeric string) |

**Optional:** Same as `create()`.

---

## Tasks

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Title` | string | Task title |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `DueAt` | string | Due date (YYYY-MM-DD) |
| `Hours` | string | Hour of task (HH) |
| `Minutes` | string | Minutes of task (MM) |
| `AssigneeId` | string | Employee ID assigned to this task |
| `DebtorId` | string | Linked customer ID |
| `DebtorContactId` | string | Linked customer contact person ID |
| `CreditorId` | string | Linked supplier ID |
| `InvoiceId` | string | Linked invoice ID |
| `PriceQuoteId` | string | Linked quote ID |
| `CreditInvoiceId` | string | Linked credit invoice ID |
| `UnprocessedCreditInvoiceId` | string | Linked unprocessed credit invoice ID |
| `SubscriptionId` | string | Linked subscription ID |
| `Description` | string | Task description |
| `Status` | string | Task status (see variables list, default: "open") |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Task ID (numeric string) |

**Optional:** Same as `create()`.

### change_status()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Task ID (numeric string) |
| `Status` | string | New status (see variables list) |

!!! info "Task Status Values"
    Common status values include: "open", "completed". Check the [WeFact variables list](https://developer.wefact.com/variables) for all available task statuses.

### attachment_add()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ReferenceIdentifier` | string | Task ID (numeric string) |
| `Type` | string | Always "crm_task" for tasks |
| `Filename` | string | Attachment filename |
| `Base64` | string | Base64 encoded file content |

### attachment_delete()

**Required (one of):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Attachment ID (numeric string) |
| `Filename` | string | **Or** attachment filename |

**Required (both):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ReferenceIdentifier` | string | Task ID (numeric string) |
| `Type` | string | Always "crm_task" for tasks |

### attachment_download()

**Required (one of):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Attachment ID (numeric string) |
| `Filename` | string | **Or** attachment filename |

**Required (both):**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ReferenceIdentifier` | string | Task ID (numeric string) |
| `Type` | string | Always "crm_task" for tasks |

!!! success "Task Attachments"
    Attachment methods use the `attachment` controller, not `task`. The download method returns an array with: `[AttachmentId, Filename, Base64Content, MimeType]`.

---

## Transactions

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `BankAccount` | string | Your bank account number (IBAN) |
| `Date` | string | Transaction date (YYYY-MM-DD) |
| `Type` | string | Transaction type: "batch", "deposit", "withdrawal", "reversal" |
| `Amount` | float | Transaction amount |
| `Currency` | string | Currency code (see variables list) |
| `Status` | string | Transaction status (see variables list) |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ShortDescription` | string | Short transaction description |
| `ExtendedDescription` | string | Extended transaction description |
| `AccountName` | string | Account holder name |
| `AccountNumber` | string | Account holder's bank account (IBAN) |
| `AccountBIC` | string | Account holder's BIC code |
| `BankReference` | string | Bank reference (auto-generated if omitted) |

!!! info "Transaction Editing"
    The WeFact API does not provide an edit endpoint for transactions. Transactions cannot be modified after creation.

---

## Groups

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Type` | string | Group type: "debtor" or "product" |
| `GroupName` | string | Group name |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Items` | array | Array of IDs for items in this group |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Group ID (numeric string) |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `GroupName` | string | Group name |
| `Items` | array | Array of IDs for items in this group |

!!! warning "Items Parameter"
    When editing a group, you must provide **all** IDs of items that should be in the group. Any items not included will be removed from the group.

---

## Cost Categories

### create()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Title` | string | Cost category title |

### edit()

**Required:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Identifier` | string | Cost category ID (numeric string) |

**Optional:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `Title` | string | Cost category title |

---

## Discount Summary

WeFact supports discounts at multiple levels:

| Level | Parameter | Applied To | Type |
|-------|-----------|------------|------|
| **Invoice Total** | `Discount` | Entire invoice | Percentage (0-100) |
| **Invoice Line** | `DiscountPercentage` | Single line item | Percentage (0-100) |
| **Subscription** | `DiscountPercentage` | Recurring invoices | Percentage (0-100) |

### Example: Invoice with Discounts

```python
client.invoices.create(
    DebtorCode="DB10001",
    Discount=10,  # 10% off entire invoice
    InvoiceLines=[
        {
            'ProductCode': 'P0001',
            'Number': 2,
            'DiscountPercentage': 5,  # Additional 5% off this line
            'DiscountPercentageType': 'line'
        }
    ]
)
```

### Example: Subscription with Discount

```python
client.subscriptions.create(
    DebtorCode="DB10001",
    Subscription={
        'ProductCode': 'P0001',
        'DiscountPercentage': 15,  # 15% off every invoice
        'Periodic': 'month'
    }
)
```

---

## Data Types

| Type | Format | Example |
|------|--------|---------|
| `string` | Text | `"DB10000"` |
| `int` | Integer | `30` |
| `float` | Decimal | `99.95` |
| `array` | Array | `["1", "2", "3"]` |
| Date | `YYYY-MM-DD` | `"2024-12-31"` |
| DateTime | `YYYY-MM-DD HH:MM:SS` | `"2024-12-31 14:30:00"` |

!!! warning "ID Format"
    All IDs are numeric strings (`"5"`), not integers (`5`).

---

## Additional Resources

- [API Resources](resources.md) - Available methods for each resource
- [API Errors](errors.md) - Error codes and handling
- [WeFact Variables](https://developer.wefact.com/variables) - Enumerated values (countries, payment methods, etc.)
