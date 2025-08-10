from enum import Enum

class Action(str, Enum):
    LIST = 'list'
    SHOW = 'show'
    ADD = 'add'
    EDIT = 'edit'
    DELETE = 'delete'
    COSTCATEGORY_LIST = 'costcategory_list'
    COSTCATEGORY_SHOW = 'costcategory_show'
    COSTCATEGORY_ADD = 'costcategory_add'
    COSTCATEGORY_EDIT = 'costcategory_edit'
    COSTCATEGORY_DELETE = 'costcategory_delete'
