from enum import Enum

class Action(str, Enum):
    LIST = 'list'
    SHOW = 'show'
    ADD = 'add'
    EDIT = 'edit'
    DELETE = 'delete'
