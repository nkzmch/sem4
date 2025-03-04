from furniture import Furniture
from elManufactory import ElementsManufactory

class Assembly:
    def __init__(self) -> None:
        self.furniture_pieces = []

    def choose_furniture_type(self) -> str:
        print("Choose type of furniture to assemble:\n1 - Table\n2 - Chair")
        choice = input()
        if choice == '1':
            return "Table"
        elif choice == '2':
            return "Chair"
        else:
            print("Invalid value")
            return "Table"

    def assemble_furniture(self, elements_manufactory: ElementsManufactory) -> None:
        if elements_manufactory.created_elements >= 2:
            furniture_type = self.choose_furniture_type()
            pieces = elements_manufactory.created_elements // 2
            elements_manufactory.created_elements -= pieces * 2
            for _ in range(pieces):
                self.furniture_pieces.append(Furniture(furniture_type))
            print(f"Assembled {pieces} pieces of {furniture_type}. "
                  f"Total furniture assembled: {len(self.furniture_pieces)}.")
        else:
            print("Not enough elements. Need at least 2 elements")
