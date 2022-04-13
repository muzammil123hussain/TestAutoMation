from tests.unit.unit_base_test import UnitBaseTest
from models.store import StoreModel


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('Test Store')
        
        self.assertEqual(store.name, 'Test Store')
