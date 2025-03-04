from assembly import Assembly

class Warehouse:
    def __init__(self) -> None:
        self.stock = 0

    def receive_furniture(self, assembly: Assembly) -> None:
        self.stock += len(assembly.furniture_pieces)
        assembly.furniture_pieces.clear()
        print(f"Received furniture in warehouse. Total stock now: {self.stock} pieces")

    def check_stock(self) -> None:
        print(f"Current stock in warehouse: {self.stock} pieces")