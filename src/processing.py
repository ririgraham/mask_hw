from datetime import datetime


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Возвращает отфильтрованный по статусу список"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, descending: bool = True) -> list:
    """Возвращает отсортированный по дате список"""
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)


"""test data"""
if __name__ == '__main__':
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    """Executing with the default status"""
    print(filter_by_state(data))

    """Executing with CANCELED status"""
    print(filter_by_state(data, "CANCELED"))

    """Executing in decsending order (by default)"""
    print(sort_by_date(data))

    """Executing in ascending order"""
    print(sort_by_date(data, descending=False))
