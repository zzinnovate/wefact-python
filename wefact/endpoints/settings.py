# File: /wefact-python/wefact-python/src/wefact/endpoints/settings.py

class SettingsEndpoint:
    def __init__(self, client):
        self.client = client

    def list(self):
        """List all settings."""
        return self.client.get('/settings')

    def show(self, identifier):
        """Show a specific setting by identifier."""
        return self.client.get(f'/settings/{identifier}')

    def update(self, identifier, data):
        """Update a specific setting by identifier."""
        return self.client.put(f'/settings/{identifier}', json=data)

    def create(self, data):
        """Create a new setting."""
        return self.client.post('/settings', json=data)

    def delete(self, identifier):
        """Delete a specific setting by identifier."""
        return self.client.delete(f'/settings/{identifier}')