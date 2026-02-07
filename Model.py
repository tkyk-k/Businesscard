import uuid
from dataclasses import dataclass

class UnacceptableValue(Exception):
    """仕様範囲外の値が渡された場合の例外"""
    pass


@dataclass(frozen=True)
class Relevance:
    department_proximity: int
    title_seniority: int
    contact_count: int
    last_contact_recency: int
    contact_people_count: int

    def __post_init__(self):
        values = [
            self.department_proximity,
            self.title_seniority,
            self.contact_count,
            self.last_contact_recency,
            self.contact_people_count,
        ]

        if any(v not in (0, 1) for v in values):
            raise UnacceptableValue("各項目は0か1でなければなりません")

        if sum(values) == 0:
            raise UnacceptableValue("すべて0は許可されません")


@dataclass(frozen=True)
class Uuid:
    value: str

    def __post_init__(self):
        try:
            uuid.UUID(self.value)
        except Exception:
            raise UnacceptableValue("UUID形式が不正です")