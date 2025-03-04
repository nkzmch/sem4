class Material:
    def __init__(self, material_type: str = None) -> None:
        self.type = material_type

    def choose_material(self) -> str:
        while True:
            print("Choose type of material:\n1 - tree\n2 - metal")
            choice = input()
            if choice == '1':
                self.type = 'tree'
                break
            elif choice == '2':
                self.type = 'metal'
                break
            else:
                print("Invalid choice")
        print("You chose type of material:", self.type)
        return self.type
