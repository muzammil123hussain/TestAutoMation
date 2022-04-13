from tests.integration.integration_base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel


class TestStore(BaseTest):
    def test_store_empty(self):
        store = StoreModel('Test Store')

        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context():
            store = StoreModel('Test Store')

            self.assertIsNone(StoreModel.find_by_name('Test Store'))
            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('Test Store'))
            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('Test Store'))

    def test_store_json(self):
        store = StoreModel('Test Store')
        expected = {
            'name': 'Test Store',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_items(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('Test Item', 20.20, 1)
            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'Test Store',
                'items': [{'name': 'Test Item', 'price': 20.20}]
            }

            self.assertDictEqual(store.json(), expected)

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('Test Item', 20.20, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'Test Item')

