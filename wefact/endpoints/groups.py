# File: /wefact-python/wefact-python/src/wefact/endpoints/groups.py

from wefact.endpoints.base import BaseEndpoint

class GroupsEndpoint(BaseEndpoint):
    def list(self, type=None):
        """
        List groups. Optionally filter by type.
        
        :param type: The type of groups to list (e.g., 'debtor').
        :return: Response from the WeFact API.
        """
        params = {}
        if type:
            params['type'] = type
        return self.get('groups', params=params)

    def create(self, group_name, type):
        """
        Create a new group.
        
        :param group_name: The name of the group to create.
        :param type: The type of group (e.g., 'debtor').
        :return: Response from the WeFact API.
        """
        data = {
            'GroupName': group_name,
            'Type': type
        }
        return self.post('groups', json=data)

    def edit(self, identifier, group_name):
        """
        Update an existing group.
        
        :param identifier: The identifier of the group to update.
        :param group_name: The new name for the group.
        :return: Response from the WeFact API.
        """
        data = {
            'Identifier': identifier,
            'GroupName': group_name
        }
        return self.put('groups', json=data)

    def show(self, identifier):
        """
        Show details of a specific group.
        
        :param identifier: The identifier of the group to show.
        :return: Response from the WeFact API.
        """
        return self.get(f'groups/{identifier}')

    def delete(self, identifier):
        """
        Delete a specific group.
        
        :param identifier: The identifier of the group to delete.
        :return: Response from the WeFact API.
        """
        return self.delete(f'groups/{identifier}')