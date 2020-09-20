from table_engine.src.table_engine_input import TableEngineInput
from django.db.models import Q, QuerySet
from typing import Optional, Iterable


class TableEngine:
    input: TableEngineInput
    model: QuerySet
    init_search_cols: Optional[list]

    def __init__(self, model, table_engine_input: dict):
        self.init_search_cols = None
        self.model = model
        self.input = TableEngineInput(table_engine_input)
        pass

    def init_cols(self, cols: list) -> 'TableEngine':
        self.init_search_cols = cols
        return self

    def init_search(self) -> None:
        if self.input.has_search():
            query = Q()
            for key in self.init_search_cols:
                query.add(Q(**{"%s__contains" % key: self.input.search}), Q.OR)
            self.model = self.model.filter(query)

    def hidden(self) -> None:
        pass

    def filter(self) -> None:
        q = Q()
        for i in self.input.filters:
            q.add(Q(**{i.lookup: i.value}), Q.AND)
        self.model = self.model.filter(q)

    def execute(self) -> dict:
        self.init_search()
        self.filter()
        self.sort()
        return {
            'rows': self.paginate(),
            'page': self.input.page,
            'count': self.total()
        }

    def paginate(self) -> Iterable:
        q = self.model.values(*[f.name for f in self.model.model._meta.fields]+self.model.model.SELECT)
        return [entry for entry in q[self.input.offset:self.input.offset + self.input.limit]]

    def total(self) -> int:
        return self.model.count()

    def sort(self) -> None:
        if self.input.has_sort():
            self.model = self.model.order_by(self.input.sort)
