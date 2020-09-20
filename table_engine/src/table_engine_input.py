from typing import Optional, Iterable
from table_engine.src.filter import TableEngineInputFilterItem


class TableEngineInput:
    __limit: Optional[int]
    __page: Optional[int]
    __search: Optional[str]
    __filters: Optional[list]
    __columns: Optional[list]
    __sort: Optional[str]

    def __init__(self, inp: dict):
        self.__sort = inp['sort'] if 'sort' in inp else None
        self.__columns = inp['columns'] if 'columns' in inp else None
        self.__filters = list(
            map(lambda item: TableEngineInputFilterItem(item), inp['filters'] if 'filters' in inp else []))
        self.__search = inp['search'] if 'search' in inp else None
        self.__page = int(inp['page']) if 'page' in inp else 0
        self.__limit = int(inp['limit']) if 'limit' in inp else 20

    def has_search(self):
        return self.__search is not None

    def has_sort(self):
        return self.__sort is not None

    @property
    def sort(self):
        return self.__sort

    @property
    def search(self):
        return self.__search

    @property
    def limit(self):
        return self.__limit

    @property
    def filters(self) -> Iterable[TableEngineInputFilterItem]:
        return self.__filters

    @property
    def columns(self):
        return self.__columns

    @property
    def page(self):
        return self.__page

    @property
    def offset(self):
        return self.__page * self.__limit
