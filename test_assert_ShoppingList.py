import unittest
from assert_ShoppingList import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})
    def test_get_item_count(self):
        self.assertEquals(self.shopping_list.get_item_count(),3)
    def test_get_total_price(self):
        self.assertEquals(self.shopping_list.get_total_price(),53)