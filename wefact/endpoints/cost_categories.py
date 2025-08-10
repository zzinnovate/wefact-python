class CostCategoriesEndpoint:
    def __init__(self, client):
        self.client = client

    def list(self):
        """List all cost categories."""
        return self.client.get('/costcategories')

    def create(self, title):
        """Create a new cost category."""
        data = {'Title': title}
        return self.client.post('/costcategories', json=data)

    def edit(self, identifier, title):
        """Update an existing cost category."""
        data = {'Identifier': identifier, 'Title': title}
        return self.client.put('/costcategories', json=data)

    def show(self, identifier):
        """Show details of a specific cost category."""
        return self.client.get(f'/costcategories/{identifier}')

    def delete(self, identifier):
        """Delete a specific cost category."""
        return self.client.delete(f'/costcategories/{identifier}')