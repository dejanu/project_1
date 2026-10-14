import unittest

import main


class ItemEndpointTests(unittest.TestCase):
    def setUp(self):
        main.db.clear()
        main.counter = 0

    def test_create_item_returns_item_with_id(self):
        item = main.create_item(main.Item(name="Widget", price=9.99))

        self.assertEqual(item, {"id": 1, "name": "Widget", "price": 9.99})

    def test_list_items_returns_created_items(self):
        main.create_item(main.Item(name="Widget", price=9.99))

        self.assertEqual(
            main.list_items(),
            [{"id": 1, "name": "Widget", "price": 9.99}],
        )


if __name__ == "__main__":
    unittest.main()