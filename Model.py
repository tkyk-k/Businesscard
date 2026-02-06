class UnacceptableValue(Exception):
    """仕様範囲外の値が渡された場合の例外"""
    pass


class Relevance:
    def __init__(self, department_proximity: int, title_seniority: int, contact_count: int, last_contact_recency: int, contact_people_count: int):
        values = [department_proximity, title_seniority, contact_count, last_contact_recency, contact_people_count]

        # 値の範囲チェック
        if any(v not in (0, 1) for v in values):
            raise UnacceptableValue("各項目は 0 か 1 でなければなりません")
        
        # すべて 0 は許可しない
        if sum(values) == 0:
            raise UnacceptableValue("すべて 0 は許可されません")
        
        self.department_proximity = department_proximity
        self.title_seniority = title_seniority
        self.contact_count = contact_count
        self.last_contact_recency = last_contact_recency
        self.contact_people_count = contact_people_count
