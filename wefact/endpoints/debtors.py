class DebtorsEndpoint:
    def __init__(self, client):
        self.client = client

    def list(self, params=None):
        """
        List all debtors.
        
        :param params: Optional parameters for filtering the list of debtors.
        :return: Response from the WeFact API.
        """
        return self.client.get('/debtors', params=params)

    def create(self, data):
        """
        Create a new debtor.
        
        :param data: Required parameters for creating a debtor.
        :return: Response from the WeFact API.
        """
        return self.client.post('/debtors', json=data)

    def edit(self, debtor_id, data):
        """
        Update an existing debtor.
        
        :param debtor_id: The ID of the debtor to update.
        :param data: Required parameters for updating the debtor.
        :return: Response from the WeFact API.
        """
        return self.client.put(f'/debtors/{debtor_id}', json=data)

    def show(self, debtor_id):
        """
        Show details of a specific debtor.
        
        :param debtor_id: The ID of the debtor to retrieve.
        :return: Response from the WeFact API.
        """
        return self.client.get(f'/debtors/{debtor_id}')

    def delete(self, debtor_id):
        """
        Delete a specific debtor.
        
        :param debtor_id: The ID of the debtor to delete.
        :return: Response from the WeFact API.
        """
        return self.client.delete(f'/debtors/{debtor_id}')