from factory import Factory  
from material import Material 
from workers import Workers

class ElementsManufactory(Factory):
    def __init__(self, workers: Workers, material: Material) -> None:
        super().__init__(workers)
        self.material = material
        self.created_elements = 0

    def prepare(self) -> None:
        if self.material.type in ['tree', 'metal']:
            print("Preparing", self.material.type, "for production")
        else:
            print("No material type")

    def work(self) -> None:
        super().work()
        print("We are preparing materials")

    def manufacture_furniture_elements(self, count: int = 2) -> None:
        if self.material.type:
            self.created_elements += count
            print(f"Manufactured {count} furniture elements from {self.material.type} "
                  f"Total: {self.created_elements} elements")
        else:
            print("No material selected. Cannot manufacture furniture elements")
