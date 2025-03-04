from workers import Workers
from material import Material
from elManufactory import ElementsManufactory
from assembly import Assembly
from warehouse import Warehouse
from control import QualityControl 
from factory import Factory  
from furniture import Furniture
def main():
    workers = Workers(10)
    material = Material()
    elements_manufactory = ElementsManufactory(workers, material)
    assembly = Assembly()
    warehouse = Warehouse()
    quality_control = QualityControl()  

    while True:
        print("Menu")
        print("1. Choose material")
        print("2. Prepare materials")
        print("3. Manufacture furniture elements")
        print("4. Check quality of elements") 
        print("5. Assemble furniture")
        print("6. Send furniture to warehouse")
        print("7. Check warehouse stock")
        print("8. Report defective elements")
        print("9. Exit\n")
        choice = input("Choose an option: ")

        if choice == '1':
            material.choose_material()
        elif choice == '2':
            elements_manufactory.prepare()
        elif choice == '3':
            count = int(input("Enter the number of elements to manufacture (default is 2): ") or 2)
            elements_manufactory.manufacture_furniture_elements(count)
        elif choice == '4':
            quality_control.check_quality(elements_manufactory)  
        elif choice == '5':
            assembly.assemble_furniture(elements_manufactory)
        elif choice == '6':
            warehouse.receive_furniture(assembly)
        elif choice == '7':
            warehouse.check_stock()
        elif choice == '8':
            quality_control.report_defects()  
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()