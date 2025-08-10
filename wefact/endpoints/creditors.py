class CreditorsEndpoint:
    def __init__(self, client):
        self.client = client

    def list(self):
        """List all creditors."""
        response = self.client.get('/creditors')
        return response

    def list_all(self):
        """List all creditors with detailed information."""
        response = self.client.get('/creditors/all')
        return response

    def create(self, company_name=None, sur_name=None):
        """Create a new creditor.

        Required parameters:
        - company_name: The name of the company (optional).
        - sur_name: The surname of the creditor (optional).
        """
        if not company_name and not sur_name:
            raise ValueError("Either 'company_name' or 'sur_name' must be provided.")
        
        data = {}
        if company_name:
            data['CompanyName'] = company_name
        if sur_name:
            data['SurName'] = sur_name
        
        response = self.client.post('/creditors', json=data)
        return response

    def update(self, identifier=None, creditor_code=None, company_name=None):
        """Update an existing creditor.

        Required parameters:
        - identifier: The identifier of the creditor (optional).
        - creditor_code: The creditor code (optional).
        """
        if not identifier and not creditor_code:
            raise ValueError("Either 'identifier' or 'creditor_code' must be provided.")
        
        data = {}
        if identifier:
            data['Identifier'] = identifier
        if creditor_code:
            data['CreditorCode'] = creditor_code
        if company_name:
            data['CompanyName'] = company_name
        
        response = self.client.put('/creditors', json=data)
        return response

    def show(self, identifier=None, creditor_code=None):
        """Show details of a specific creditor.

        Required parameters:
        - identifier: The identifier of the creditor (optional).
        - creditor_code: The creditor code (optional).
        """
        if not identifier and not creditor_code:
            raise ValueError("Either 'identifier' or 'creditor_code' must be provided.")
        
        params = {}
        if identifier:
            params['Identifier'] = identifier
        if creditor_code:
            params['CreditorCode'] = creditor_code
        
        response = self.client.get('/creditors/show', params=params)
        return response

    def delete(self, identifier=None, creditor_code=None):
        """Delete a creditor.

        Required parameters:
        - identifier: The identifier of the creditor (optional).
        - creditor_code: The creditor code (optional).
        """
        if not identifier and not creditor_code:
            raise ValueError("Either 'identifier' or 'creditor_code' must be provided.")
        
        params = {}
        if identifier:
            params['Identifier'] = identifier
        if creditor_code:
            params['CreditorCode'] = creditor_code
        
        response = self.client.delete('/creditors', params=params)
        return response