from django.db.models import QuerySet

from const.model.const import Const
from const.model.crel import CRel


class IConst:
    @staticmethod
    def get_title(const_id: int):
        pass

    @staticmethod
    def set(title: object, key: object, left: object = None) -> object:
        const = Const.objects.create(title=title, k=key)
        if left is not None:
            CRel.objects.create(left_id=left, right=const)
        return const

    @staticmethod
    def update(title: str, k: int):
        pass

    @staticmethod
    def get_by_key(key: int) -> QuerySet:
        return Const.objects.filter(k=key)

    @staticmethod
    def get_by_left(const_id: int) -> QuerySet:
        return Const.objects.filter(right__left=const_id)
