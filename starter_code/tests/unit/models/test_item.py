from tests.unit.unit_base_test import UnitBaseTest
from models.item import ItemModel


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test', 20.20, 1)

        self.assertEqual(item.name, 'test', 'Item name Error')
        self.assertEqual(item.price, 20.20, 'Item price Error')
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test', 20.20, 1)

        expected = {
            'name': 'test',
            'price': 20.20
        }

        self.assertEqual(item.json(), expected, "item.json is {} and expected is {} ".format(item.json(), expected))
