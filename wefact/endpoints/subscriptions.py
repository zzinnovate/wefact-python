# File: /wefact-python/wefact-python/src/wefact/endpoints/subscriptions.py

from wefact.endpoints.base import BaseEndpoint

class Subscriptions(BaseEndpoint):
    def list(self, **kwargs):
        """List all subscriptions."""
        return self.client.get('/subscriptions', params=kwargs)

    def create(self, debtor_code, product_code=None, description=None, price_excl=None, periodic=None, terminate_after=None):
        """Create a new subscription."""
        data = {
            'DebtorCode': debtor_code,
            'ProductCode': product_code,
            'Description': description,
            'PriceExcl': price_excl,
            'Periodic': periodic,
            'TerminateAfter': terminate_after
        }
        return self.client.post('/subscriptions', json=data)

    def edit(self, subscription_id, description=None, price_excl=None, periodic=None, terminate_after=None):
        """Update an existing subscription."""
        data = {
            'Description': description,
            'PriceExcl': price_excl,
            'Periodic': periodic,
            'TerminateAfter': terminate_after
        }
        return self.client.put(f'/subscriptions/{subscription_id}', json=data)

    def show(self, subscription_id):
        """Show details of a specific subscription."""
        return self.client.get(f'/subscriptions/{subscription_id}')

    def terminate(self, subscription_id):
        """Terminate a subscription."""
        return self.client.delete(f'/subscriptions/{subscription_id}')