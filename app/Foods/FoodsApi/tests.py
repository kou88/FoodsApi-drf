from django.test import TestCase
from FoodsApi import views

class HowToTestCase(TestCase):
    """ はじめてのテスト """
    def test_returnTrue(self):
        self.assertIs(views.HowToTest.returnTrue(), True)
