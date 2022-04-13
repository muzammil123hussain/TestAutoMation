from models.item import ItemModel
from models.store import StoreModel
from tests.integration.integration_base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()
            item = ItemModel('test', 20.20, 1)

            self.assertIsNone(ItemModel.find_by_name('test'))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test_Store').save_to_db()
            item = ItemModel('test', 20.20, 1).save_to_db()

            self.assertEqual(item.store.name, 'Test Store')
