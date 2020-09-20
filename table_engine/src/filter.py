from typing import Optional, Any


class TableEngineInputFilterItem:
    __value: Optional[Any]
    __op: Optional[str]
    __field: Optional[str]
    __op_map: dict = {
        'sw': 'startswith',
        'ew': 'endswith',
        'like': 'contains',
        'in': 'in',
        'gt': 'gt',
        'gte': 'gte',
        'lt': 'lt',
        'lte': 'lte',
    }

    def __init__(self, inp):
        self.__field = inp['field'] if 'field' in inp else None
        self.__op = inp['op'] if 'op' in inp else 'contains'
        self.__value = inp['value'] if 'value' in inp else None
        self.__con = inp['con'] if 'con' in inp else 'AND'

    def has_op(self):
        return self.__op is not None

    @property
    def op(self):
        return self.__op

    @property
    def lookup(self):
        op = self.__op_map[self.op] if self.op in self.__op_map else self.op
        return self.field + '__' + op

    @property
    def value(self):
        return self.__value

    @property
    def field(self):
        return self.__field