class Furniture:
    def __init__(self, furniture_type: str) -> None:
        self.furniture_type = furniture_type

    def __str__(self) -> str:
        return self.furniture_type
