from __future__ import annotations

from typing import Any, Dict, List

from .request import RequestMixin
from .enums import Action, InvoiceAction
from .exceptions import ClientError


class BaseResource(RequestMixin):
    controller_name: str

    def __init__(self, api_key: str, api_url: str = "https://api.mijnwefact.nl/v2/"):
        self.api_key = api_key
        self.api_url = api_url

    def list(self, **params) -> Dict[str, Any]:
        return self._send_request(self.controller_name, Action.LIST.value, params)

    def list_all(self, offset: int = 0, per_page: int = 1000) -> List[Dict[str, Any]]:
        limit_per_second = 300 / 60
        calls = 1
        data: List[Dict[str, Any]] = []
        plural_name = self.get_plural_resource_name()

        result = self.list(limit=per_page, offset=offset)

        for index, item in enumerate(result.get(plural_name, [])):
            calls += 1
            if calls % limit_per_second == 0:
                import time

                time.sleep(1)
            detail = self.show(Identifier=item["Identifier"])
            if isinstance(detail, dict) and self.controller_name in detail:
                result[plural_name][index] = detail[self.controller_name]
        data.extend(result.get(plural_name, []))
        if result.get("currentresults", 0) >= per_page:
            data.extend(self.list_all(offset + per_page, per_page))
        return data

    def show(self, **params) -> Dict[str, Any]:
        return self._send_request(self.controller_name, Action.SHOW.value, params)

    def create(self, **params) -> Dict[str, Any]:
        return self._send_request(self.controller_name, Action.ADD.value, params)

    def edit(self, **params) -> Dict[str, Any]:
        return self._send_request(self.controller_name, Action.EDIT.value, params)

    def delete(self, **params) -> Dict[str, Any]:
        return self._send_request(self.controller_name, Action.DELETE.value, params)

    def get_plural_resource_name(self) -> str:
        return f"{self.controller_name}s"


class InvoiceResource(BaseResource):
    controller_name = "invoice"

    def credit(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.CREDIT.value, params
        )

    def part_payment(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.PART_PAYMENT.value, params
        )

    def mark_as_paid(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.MARK_AS_PAID.value, params
        )

    def mark_as_unpaid(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.MARK_AS_UNPAID.value, params
        )

    def send_by_email(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.SEND_BY_EMAIL.value, params
        )

    def send_reminder_by_email(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.SEND_REMINDER_BY_EMAIL.value, params
        )

    def send_summation_by_email(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.SEND_SUMMATION_BY_EMAIL.value, params
        )

    def download(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.DOWNLOAD.value, params
        )

    def block(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.BLOCK.value, params
        )

    def unblock(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.UNBLOCK.value, params
        )

    def schedule(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.SCHEDULE.value, params
        )

    def cancel_schedule(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.CANCEL_SCHEDULE.value, params
        )

    def payment_process_pause(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.PAYMENT_PROCESS_PAUSE.value, params
        )

    def payment_process_reactivate(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.PAYMENT_PROCESS_REACTIVATE.value, params
        )

    def sort_lines(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.SORT_LINES.value, params
        )

    def invoice_line_add(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.INVOICE_LINE_ADD.value, params
        )

    def invoice_line_delete(self, **params):
        return self._send_request(
            self.controller_name, InvoiceAction.INVOICE_LINE_DELETE.value, params
        )

    def attachment_add(self, **params):
        params["Type"] = self.controller_name
        return self._send_request(
            self.controller_name, InvoiceAction.ATTACHMENT_ADD.value, params
        )

    def attachment_delete(self, **params):
        params["Type"] = self.controller_name
        return self._send_request(
            self.controller_name, InvoiceAction.ATTACHMENT_DELETE.value, params
        )

    def attachment_download(self, **params):
        params["Type"] = self.controller_name
        return self._send_request(
            self.controller_name, InvoiceAction.ATTACHMENT_DOWNLOAD.value, params
        )


class DebtorResource(BaseResource):
    controller_name = "debtor"

    def delete(self, **params):  # Not available
        raise ClientError("delete is not available for this resource.")


class ProductResource(BaseResource):
    controller_name = "product"


class CreditorResource(BaseResource):
    controller_name = "creditor"


class GroupResource(BaseResource):
    controller_name = "group"


class SubscriptionResource(BaseResource):
    controller_name = "subscription"

    def delete(self, **params):
        raise ClientError("delete is not available for this resource.")

    def terminate(self, **params):
        from .enums.subscription_actions import SubscriptionAction

        return self._send_request(
            self.controller_name, SubscriptionAction.TERMINATE.value, params
        )


class InteractionResource(BaseResource):
    controller_name = "interaction"

    def attachment_add(self, **params):
        # Some endpoints require a Type; Interactions API may infer it from Identifier context
        from .enums import InteractionAction

        return self._send_request(
            self.controller_name, InteractionAction.ATTACHMENT_ADD.value, params
        )

    def attachment_delete(self, **params):
        from .enums import InteractionAction

        return self._send_request(
            self.controller_name, InteractionAction.ATTACHMENT_DELETE.value, params
        )

    def attachment_download(self, **params):
        from .enums import InteractionAction

        return self._send_request(
            self.controller_name, InteractionAction.ATTACHMENT_DOWNLOAD.value, params
        )


class SettingsResource(BaseResource):
    controller_name = "settings"

    def get_plural_resource_name(self) -> str:
        return self.controller_name

    def show(self, **params):
        raise ClientError("show is not available for this resource.")

    def create(self, **params):
        raise ClientError("create is not available for this resource.")

    def edit(self, **params):
        raise ClientError("edit is not available for this resource.")

    def delete(self, **params):
        raise ClientError("delete is not available for this resource.")


class CostCategoryResource(BaseResource):
    controller_name = "costcategory"

    def get_plural_resource_name(self) -> str:
        return "costcategories"

    def list(self, **params):
        from .enums.cost_category_actions import CostCategoryAction

        return self._send_request(
            self.controller_name, CostCategoryAction.LIST.value, params
        )

    def show(self, **params):
        from .enums.cost_category_actions import CostCategoryAction

        return self._send_request(
            self.controller_name, CostCategoryAction.SHOW.value, params
        )

    def create(self, **params):
        from .enums.cost_category_actions import CostCategoryAction

        return self._send_request(
            self.controller_name, CostCategoryAction.ADD.value, params
        )

    def edit(self, **params):
        from .enums.cost_category_actions import CostCategoryAction

        return self._send_request(
            self.controller_name, CostCategoryAction.EDIT.value, params
        )

    def delete(self, **params):
        from .enums.cost_category_actions import CostCategoryAction

        return self._send_request(
            self.controller_name, CostCategoryAction.DELETE.value, params
        )
