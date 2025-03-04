import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from workers import Workers
from material import Material
from elManufactory import ElementsManufactory
from assembly import Assembly
from warehouse import Warehouse
from control import QualityControl 
from factory import Factory  
from furniture import Furniture

class TestWorkers(unittest.TestCase):
    def test_initialization(self):
        workers = Workers(10)
        self.assertEqual(workers.number, 10)

    def test_set_number(self):
        workers = Workers(5)
        workers.number = 15
        self.assertEqual(workers.number, 15)

    def test_negative_number(self):
        workers = Workers(-5)
        self.assertEqual(workers.number, -5)

class TestFactory(unittest.TestCase):
    def setUp(self):
        self.workers = Workers(10)
        self.factory = Factory(self.workers)

    def test_initialization(self):
        self.assertEqual(self.factory.workers.number, 10)

    @patch('builtins.print')
    def test_number_of_workers(self, mock_print):
        self.factory.number_of_workers()
        mock_print.assert_called_once_with("Number of workers:", 10)

    @patch('builtins.print')
    def test_work_method(self, mock_print):
        self.factory.work()
        mock_print.assert_called_once_with("We are working")

class TestElementsManufactory(unittest.TestCase):
    def setUp(self):
        self.workers = Workers(10)
        self.material = Material("tree")
        self.manufactory = ElementsManufactory(self.workers, self.material)

    def test_initialization(self):
        self.assertEqual(self.manufactory.workers.number, 10)
        self.assertEqual(self.manufactory.material.type, "tree")
        self.assertEqual(self.manufactory.created_elements, 0)

    @patch('builtins.print')
    def test_prepare_with_valid_material(self, mock_print):
        self.manufactory.prepare()
        mock_print.assert_called_once_with("Preparing", "tree", "for production")

    @patch('builtins.print')
    def test_prepare_with_invalid_material(self, mock_print):
        self.manufactory.material.type = None
        self.manufactory.prepare()
        mock_print.assert_called_once_with("No material type")

    @patch('builtins.print')
    def test_work_method(self, mock_print):
        self.manufactory.work()
        mock_print.assert_any_call("We are working")
        mock_print.assert_any_call("We are preparing materials")

    @patch('builtins.print')
    def test_manufacture_furniture_elements(self, mock_print):
        self.manufactory.manufacture_furniture_elements(5)
        mock_print.assert_called_once_with(
            "Manufactured 5 furniture elements from tree Total: 5 elements"
        )
        self.assertEqual(self.manufactory.created_elements, 5)

    @patch('builtins.print')
    def test_manufacture_without_material(self, mock_print):
        self.manufactory.material.type = None
        self.manufactory.manufacture_furniture_elements(5)
        mock_print.assert_called_once_with("No material selected. Cannot manufacture furniture elements")
        self.assertEqual(self.manufactory.created_elements, 0)

class TestWarehouse(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse()
        self.assembly = Assembly()
        self.assembly.furniture_pieces.append(Furniture("Chair"))
        self.assembly.furniture_pieces.append(Furniture("Table"))
    
    @patch('builtins.print')  
    def test_receive_furniture(self, mock_print):
        self.assertEqual(self.warehouse.stock, 0)
        self.warehouse.receive_furniture(self.assembly)
        self.assertEqual(self.warehouse.stock, 2)
        self.assertEqual(len(self.assembly.furniture_pieces), 0)
        mock_print.assert_called_once_with("Received furniture in warehouse. Total stock now: 2 pieces")

    @patch('builtins.print') 
    def test_check_stock(self, mock_print):
        self.warehouse.stock = 5  
        self.warehouse.check_stock()
        mock_print.assert_called_once_with("Current stock in warehouse: 5 pieces")

class TestQualityControl(unittest.TestCase):
    def setUp(self):
        self.quality_control = QualityControl()
        self.elements_manufactory = ElementsManufactory(workers=5, material=Material("tree"))

    @patch('builtins.print')
    def test_check_quality_with_defective_elements(self, mock_print):
        self.elements_manufactory.created_elements = 25
        
        self.quality_control.check_quality(self.elements_manufactory)

        self.assertEqual(self.quality_control.defective_elements, 2)
        self.assertEqual(self.elements_manufactory.created_elements, 23)
        mock_print.assert_called_once_with("Quality control: Found 2 defective elements Remaining good elements: 23")

    @patch('builtins.print')
    def test_check_quality_no_elements(self, mock_print):
        self.elements_manufactory.created_elements = 0
        
        self.quality_control.check_quality(self.elements_manufactory)

        self.assertEqual(self.quality_control.defective_elements, 0)
        mock_print.assert_called_once_with("No elements to check")

    @patch('builtins.print')
    def test_report_defects(self, mock_print):
        self.quality_control.defective_elements = 5
        
        self.quality_control.report_defects()

        mock_print.assert_called_once_with("Total defective elements found: 5")

class TestMaterial(unittest.TestCase):
    def test_choose_material_tree(self):
        material = Material()
        with patch('builtins.input', return_value='1'), patch('builtins.print'): 
            result = material.choose_material()
            self.assertEqual(result, 'tree')
            self.assertEqual(material.type, 'tree')

    def test_choose_material_metal(self):
        material = Material()
        with patch('builtins.input', return_value='2'), patch('builtins.print'):  
            result = material.choose_material()
            self.assertEqual(result, 'metal')
            self.assertEqual(material.type, 'metal')

    def test_choose_material_invalid_then_valid(self):
        material = Material()
        with patch('builtins.input', side_effect=['3', '1']), patch('builtins.print'):  
            result = material.choose_material()
            self.assertEqual(result, 'tree')
            self.assertEqual(material.type, 'tree')

    def test_choose_material_default_none(self):
        material = Material()
        self.assertIsNone(material.type)

class TestFurniture(unittest.TestCase):
    def test_initialization(self):
        furniture = Furniture("Chair")
        self.assertEqual(furniture.furniture_type, "Chair")

    def test_str_method(self):
        furniture = Furniture("Table")
        self.assertEqual(str(furniture), "Table")

if __name__ == '__main__':
    unittest.main()

