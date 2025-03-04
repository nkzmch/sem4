from elManufactory import ElementsManufactory 
from warehouse import Warehouse  

class QualityControl:
    def __init__(self) -> None:
        self.defective_elements = 0  

    def check_quality(self, elements_manufactory: ElementsManufactory) -> None:

        if elements_manufactory.created_elements > 0:
            
            defective = elements_manufactory.created_elements // 10
            self.defective_elements += defective
            elements_manufactory.created_elements -= defective
            print(f"Quality control: Found {defective} defective elements "
                  f"Remaining good elements: {elements_manufactory.created_elements}")
        else:
            print("No elements to check")

    def report_defects(self) -> None:
       
        print(f"Total defective elements found: {self.defective_elements}")