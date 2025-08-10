class BaseEndpoint:
    def __init__(self, client):
        self.client = client

    def _get(self, endpoint, params=None):
        return self.client.get(endpoint, params)

    def _post(self, endpoint, data=None):
        return self.client.post(endpoint, data)

    def _put(self, endpoint, data=None):
        return self.client.put(endpoint, data)

    def _delete(self, endpoint):
        return self.client.delete(endpoint)