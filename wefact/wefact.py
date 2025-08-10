from __future__ import annotations

from .resources import (
    InvoiceResource,
    DebtorResource,
    ProductResource,
    CreditorResource,
    GroupResource,
    SubscriptionResource,
    SettingsResource,
    CostCategoryResource,
)


class WeFact:
    def __init__(self, api_key: str, api_url: str = "https://api.mijnwefact.nl/v2/"):
        self.api_key = api_key
        self.api_url = api_url

    @property
    def invoices(self) -> InvoiceResource:
        return InvoiceResource(self.api_key, self.api_url)

    @property
    def debtors(self) -> DebtorResource:
        return DebtorResource(self.api_key, self.api_url)

    @property
    def products(self) -> ProductResource:
        return ProductResource(self.api_key, self.api_url)

    @property
    def creditors(self) -> CreditorResource:
        return CreditorResource(self.api_key, self.api_url)

    @property
    def groups(self) -> GroupResource:
        return GroupResource(self.api_key, self.api_url)

    @property
    def subscriptions(self) -> SubscriptionResource:
        return SubscriptionResource(self.api_key, self.api_url)

    @property
    def settings(self) -> SettingsResource:
        return SettingsResource(self.api_key, self.api_url)

    @property
    def cost_categories(self) -> CostCategoryResource:
        return CostCategoryResource(self.api_key, self.api_url)
