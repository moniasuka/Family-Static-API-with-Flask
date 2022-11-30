
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        adding_member = {}
        if 'id' in member:
            member['id']
            adding_member['id'] = int(member['id'])
        else:
            adding_member['id'] = self._generateId()

        adding_member['first_name'] = str(member['first_name'])
        adding_member['last_name'] = self.last_name
        adding_member['age'] = int(member['age'])
        adding_member['lucky_numbers'] = member['lucky_numbers']
        self._members.append(adding_member)
        print(self._members)
        return None

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]['id'] == int(id):
                self._members.pop(position)
                return {"mensaje: " : "Miembro eliminado"}
        return {"done": "Miembro no encontrado"}
        

    def get_member(self, id):
        # fill this method and update the return
        for miembro in self._members:
            if miembro["id"] == int(id):
                return miembro
        
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
